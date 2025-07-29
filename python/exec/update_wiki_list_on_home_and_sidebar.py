import sys
import os
import shutil
import glob
sys.path.append('./src')

from home import Home
from sidebar import Sidebar

_, genre, language, *_ = sys.argv

print('-------------------- Categorising the Entire github-wiki-organisers Wiki Pages... --------------------')
print()
print('-------------------- Organising Home... --------------------')
match genre:
    case '-o' | '--owner' | '-c' | '--category':
        home_url = Home(genre = genre).run()

        match language:
            case '-en' | '-ja':
                home_url = Home(genre = genre, language = language).run()
    case _:
        home_url = Home().run()
print(f"Check out an Up-to-date Wiki List on Home at '{home_url}' !!")
print('-------------------- Done Organising Home 🎉 --------------------')
print()
print('-------------------- Organising Sidebar... --------------------')
match genre:
    case '-o' | '--owner' | '-c' | '--category':
        Sidebar(genre = genre).run()

        match language:
            case '-en' | '-ja':
                Sidebar(genre = genre, language = language).run()
    case _:
        Sidebar().run()
print(f"Check out an Up-to-date Wiki List on Sidebar at '{home_url}' !!")
print('-------------------- Done Organising Sidebar 🎉 --------------------')
print()
print('-------------------- Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 --------------------')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
