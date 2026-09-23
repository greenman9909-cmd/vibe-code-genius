# -*- mode: python ; coding: utf-8 -*-
a=Analysis(["vibe_code_genius/desktop.py"],pathex=[],binaries=[],datas=[],hiddenimports=["vibe_code_genius.project_engine","vibe_code_genius.project_graph","vibe_code_genius.git_engine","vibe_code_genius.agent_gateway","vibe_code_genius.mission_engine"],hookspath=[],hooksconfig={},runtime_hooks=[],excludes=[],noarchive=False)
pyz=PYZ(a.pure)
exe=EXE(pyz,a.scripts,a.binaries,a.datas,[],name="GodTreeOS",debug=False,bootloader_ignore_signals=False,strip=False,upx=True,console=False,disable_windowed_traceback=False)
