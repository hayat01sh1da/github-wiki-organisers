import sys
import os
import shutil
import glob
sys.path.append('./src')

from unknown_wiki_list_exporter_for_llm import UnknownWikiListExporterForLLM

_, group_by, language, *_ = sys.argv
params = dict()
for key, value in { 'group_by': group_by, 'language': language }.items():
    if value:
        params[key] = value

print('-------------------- Exporting Unknown Wiki List... --------------------')
path_to_export = UnknownWikiListExporterForLLM(**params).run()
print()
print(f"Check it out result on '{path_to_export}' !!")
print()
print('-------------------- Done Exporting Unknown Wiki List 🎉 --------------------')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
