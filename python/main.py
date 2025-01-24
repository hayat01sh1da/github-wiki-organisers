import sys
import os
import shutil
import glob
sys.path.append('./src')

from directory import Directory
from home import Home
from sidebar import Sidebar

print('==================== Categorizing the Entire aya-issues Wiki Pages... ====================')

print('========== Tidying Home... ==========')
home_url = Home().run()
print('Check out An Up-to-date Wiki List on Home at {home_url} !!'.format(home_url = home_url))
print('========== Done Tidying Home 🎉 ==========\n')

print('========== Tidying Sidebar... ==========')
Sidebar().run()
print('Check out An Up-to-date Wiki List on Sidebar at {home_url} !!'.format(home_url = home_url))
print('==================== Done Categorizing the Entire aya-issues Wiki Pages 🎉 ====================')
print('========== Done Tidying Sidebar 🎉 ==========\n')

print('==================== Done Categorizing the Entire aya-issues Wiki Pages 🎉 ====================')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
