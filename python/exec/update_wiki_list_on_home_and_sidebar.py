import sys
import os
import shutil
import glob
sys.path.append('./src')

from home import Home
from sidebar import Sidebar

_, group_by, language, home_overflow, *_ = sys.argv

print('-------------------- Categorising the Entire github-wiki-organisers Wiki Pages... --------------------')
print()
print('-------------------- Organising Home... --------------------')
match group_by:
    case 'Owner' | 'Category':
        match language:
            case 'English' | 'Japanese':
                if home_overflow == 'true':
                    home_url = Home(group_by = group_by, language = language, home_overflow = True).run()
                else:
                    home_url = Home(group_by = group_by, language = language).run()
    case _:
        home_url = Home().run()
print(f"Check out an Up-to-date Wiki List on Home at '{home_url}' !!")
print('-------------------- Done Organising Home 🎉 --------------------')
print()
print('-------------------- Organising Sidebar... --------------------')
match group_by:
    case 'Owner' | 'Category':
        Sidebar(group_by = group_by).run()

        match language:
            case 'English' | 'Japanese':
                Sidebar(group_by = group_by, language = language).run()
    case _:
        Sidebar().run()
print(f"Check out an Up-to-date Wiki List on Sidebar at '{home_url}' !!")
print('-------------------- Done Organising Sidebar 🎉 --------------------')
print()
print('-------------------- Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 --------------------')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
