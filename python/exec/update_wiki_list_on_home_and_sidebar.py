import sys
import os
import shutil
import glob
sys.path.append('./src')

from home import Home
from sidebar import Sidebar

base_path    = os.path.join('..', '..')
_, genre, *_ = sys.argv

print('==================== Categorizing the Entire github-wiki-organisers Wiki Pages... ====================')

print('========== Organising Home... ==========')
home_url = Home(base_path = base_path, genre = genre).run()
print(f'Check out An Up-to-date Wiki List on Home at {home_url} !!')
print('========== Done Organising Home 🎉 ==========\n')

print('========== Organising Sidebar... ==========')
Sidebar(base_path= base_path, genre = genre).run()
print(f'Check out An Up-to-date Wiki List on Sidebar at {home_url} !!')
print('==================== Done Categorizing the Entire github-wiki-organisers Wiki Pages 🎉 ====================')
print('========== Done Organising Sidebar 🎉 ==========\n')

print('==================== Done Categorizing the Entire github-wiki-organisers Wiki Pages 🎉 ====================')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
