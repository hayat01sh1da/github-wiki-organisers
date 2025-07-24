import sys
import os
import shutil
import glob
sys.path.append('./src')

from unknown_wiki_count_list_exporter import UnknownWikiCountListExporter

base_path    = os.path.join('..', '..')
_, genre, *_ = sys.argv

print('==================== Exporting Unknown Wiki Count List... ====================')
print('========== Organising Home... ==========')
count_list_by_namespace, path_to_export = UnknownWikiCountListExporter(base_path = base_path, genre = genre).run()
print('Here is the result:\n\n')

print(count_list_by_namespace)

print(f"\nCheck it out result on '{path_to_export}' !!")
print('==================== Done Exporting Unknown Wiki Count List 🎉 ====================')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
