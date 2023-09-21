from __future__ import annotations

import os
import re
from os.path import join
from pprint import pprint

pattern = r"img\/[a-zA-Z-]+\/[a-zA-Z]+\/([a-zA-Z0-9_-]+\.(?:jpg|png))"

used_imgs = []
with open("index.html", "r") as f:
    for line in f.readlines():
        line = line.strip()
        matches = re.findall(pattern, line)
        if len(matches) == 0:
            continue
        used_imgs += matches
used_imgs = set(used_imgs)

print("Images used:")
pprint(used_imgs)

for root, dirs, files in os.walk("img", topdown=False):
    if root == "img":
        continue
    if "logo" in root:
        continue
    for f in files:
        if f not in used_imgs:
            fpath = join(root, f)
            os.remove(join(root, f))
            print(f"Removed {fpath}")
