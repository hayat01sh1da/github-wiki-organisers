import sys
import os
import shutil
import glob
sys.path.append('./src')

from directory import Directory
from home import Home
from sidebar import Sidebar

print('==================== Categosizing the Entire aya-issues Wiki pages... ====================')
Directory().run
Home().run
Sidebar().run
print('==================== Done categorising the Entire aya-issues Wiki pages 🎉 ====================')

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
