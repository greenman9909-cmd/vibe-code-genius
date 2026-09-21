#!/usr/bin/env python3
import json, sys
from pathlib import Path
args=sys.argv[1:]; root=Path(__file__).resolve().parents[1]; structure=json.loads(Path(args[0]).read_text()) if args else {}; product=json.loads(Path(args[1]).read_text()) if len(args)>1 else {}
out=Path(args[2]) if len(args)>2 else Path('prompt.md'); lines=['# Build Prompt','',f"Product: {product.get('product_type','custom')}",f"Reference: {structure.get('reference_url','none')}",'','## Routes']
lines += [f"- {r.get('path')} — {r.get('title','untitled')}" for r in structure.get('routes',[])]
lines += ['', '## Build instructions', 'Use the declared route map, tokens, components, and API surface. Do not invent pages or proof.']
out.write_text('\n'.join(lines)+'\n'); print(out)
