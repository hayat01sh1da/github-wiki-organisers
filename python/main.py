import sys
import os
import shutil
import glob
sys.path.append('./src')

from directory import Directory
from home import Home
from sidebar import Sidebar

print('==================== Categorizing the Entire aya-issues Wiki Pages... ====================')

print('========== Tidying Directories... ==========')
mkdir_results, mv_wikis_to_dir_results, delete_empty_dir_results = Directory().run()
print('===== Making Directories by Owner Unit... =====')
for mkdir_result in mkdir_results:
    print(mkdir_result)
print('===== Done Making Directories by Owner Unit 🎉 =====\n')

print("===== Moving Files to Owner's Directories... =====")
for mv_wikis_to_dir_result in mv_wikis_to_dir_results:
    print(mv_wikis_to_dir_result)
print("===== Done Moving Files to Owner's Directories 🎉 =====\n")

print('===== Deleting Empty Directories... =====')
for delete_empty_dir_result in delete_empty_dir_results:
    print(delete_empty_dir_result)
print('===== Done Deleting Empty Directories 🎉 =====')
print('========== Done Tidying Directories 🎉 ==========\n')

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
