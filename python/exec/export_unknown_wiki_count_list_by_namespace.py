import sys
import os
import shutil
import glob
sys.path.append('../src')
from unknown_wiki_count_list_exporter import UnknownWikiCountListExporter

_, genre, *_ = sys.argv

print('==================== Exporting Unknown Wiki List... ====================')
print('========== Organising Home... ==========')
count_list_by_namespace, path_to_export = UnknownWikiCountListExporter(genre = genre).run()
print('Here is the result:\n\n')

print(count_list_by_namespace)

print("\nCheck it out result on '{path_to_export}' !!".format(path_to_export = path_to_export))
print('==================== Done Exporting Unknown Wiki List 🎉 ====================')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
