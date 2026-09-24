use serde::Serialize;
use std::{fs, path::{Path, PathBuf}, process::Command};

#[derive(Serialize)]
struct ProjectSnapshot {
    workspace: String,
    name: String,
    branch: Option<String>,
    dirty: bool,
    changed_files: Vec<String>,
    godtree_store: bool,
}

fn checked_workspace(input: &str) -> Result<PathBuf, String> {
    let path = Path::new(input).canonicalize().map_err(|e| e.to_string())?;
    if !path.is_dir() { return Err("workspace is not a directory".into()); }
    Ok(path)
}

fn git(workspace: &Path, args: &[&str]) -> Option<String> {
    let out = Command::new("git").arg("-C").arg(workspace).args(args).output().ok()?;
    if !out.status.success() { return None; }
    Some(String::from_utf8_lossy(&out.stdout).trim().to_string())
}

#[tauri::command]
fn inspect_project(workspace: String) -> Result<ProjectSnapshot, String> {
    let root = checked_workspace(&workspace)?;
    let status = git(&root, &["status", "--porcelain"]).unwrap_or_default();
    let changed_files = status.lines().filter_map(|line| line.get(3..).map(str::to_owned)).collect::<Vec<_>>();
    Ok(ProjectSnapshot {
        workspace: root.display().to_string(),
        name: root.file_name().and_then(|v| v.to_str()).unwrap_or("project").to_owned(),
        branch: git(&root, &["branch", "--show-current"]).filter(|s| !s.is_empty()),
        dirty: !changed_files.is_empty(),
        changed_files,
        godtree_store: root.join(".godtree").is_dir(),
    })
}

#[tauri::command]
fn read_missions(workspace: String) -> Result<Vec<serde_json::Value>, String> {
    let root = checked_workspace(&workspace)?;
    let dir = root.join(".godtree").join("missions");
    if !dir.exists() { return Ok(vec![]); }
    let mut missions = vec![];
    for entry in fs::read_dir(dir).map_err(|e| e.to_string())? {
        let path = entry.map_err(|e| e.to_string())?.path();
        if path.extension().and_then(|v| v.to_str()) != Some("json") { continue; }
        let body = fs::read_to_string(path).map_err(|e| e.to_string())?;
        missions.push(serde_json::from_str(&body).map_err(|e| e.to_string())?);
    }
    Ok(missions)
}

#[tauri::command]
fn git_diff(workspace: String) -> Result<String, String> {
    let root = checked_workspace(&workspace)?;
    git(&root, &["diff", "--stat"]).ok_or_else(|| "git diff failed".into())
}

pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![inspect_project, read_missions, git_diff])
        .run(tauri::generate_context!())
        .expect("error while running GodTree");
}
