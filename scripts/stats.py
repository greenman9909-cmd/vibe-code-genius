#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path
counts=Counter(); models=Counter()
for path in Path('.').glob('**/session.log'):
    for line in path.read_text(errors='ignore').splitlines():
        try:
            row=json.loads(line); counts[row.get('node','unknown')]+=1; models[(row.get('node','unknown'),row.get('model','unknown'))]+=1
        except json.JSONDecodeError:
            continue
print('Top failures:')
for node,count in counts.most_common(5): print(node,count,models.most_common())
