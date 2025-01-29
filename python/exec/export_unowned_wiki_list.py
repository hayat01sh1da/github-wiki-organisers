import sys
import os
import shutil
import glob
sys.path.append('../src')
from unowned_wiki_list_exporter import UnknownWikiListExporter

print('==================== Exporting Unowned Wiki List... ====================')
print('========== Organising Home... ==========')
count_lists_by_namespace, path_to_export = UnknownWikiListExporter().run()
print('Here is the result:\n\n')

print(count_lists_by_namespace)

print("\nCheck it out result on '{path_to_export}' !!".format(path_to_export = path_to_export))
print('==================== Done Exporting Unowned Wiki List 🎉 ====================')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
