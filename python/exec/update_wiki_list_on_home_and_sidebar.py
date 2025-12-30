import sys
import os
import shutil
import glob
sys.path.append('./src')

from home import Home
from sidebar import Sidebar

_, group_by, language, home_overflow, *_ = sys.argv
params = dict()
for key, value in { 'group_by': group_by, 'language': language, 'home_overflow': home_overflow }.items():
    if value:
        params[key] = value

print('-------------------- Categorising the Entire github-wiki-organisers Wiki Pages... --------------------')
print()
print('-------------------- Organising Home... --------------------')
home_url = Home(**params).run()
print(f"Check out an Up-to-date Wiki List on Home at '{home_url}' !!")
print('-------------------- Done Organising Home 🎉 --------------------')
print()
print('-------------------- Organising Sidebar... --------------------')
Sidebar(**params).run()
print(f"Check out an Up-to-date Wiki List on Sidebar at '{home_url}' !!")
print('-------------------- Done Organising Sidebar 🎉 --------------------')
print()
print('-------------------- Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 --------------------')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
