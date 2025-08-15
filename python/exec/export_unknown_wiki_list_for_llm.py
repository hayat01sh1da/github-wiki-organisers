import sys
import os
import shutil
import glob
sys.path.append('./src')

from unknown_wiki_list_exporter_for_llm import UnknownWikiListExporterForLLM

_, group_by, language, *_ = sys.argv

print('-------------------- Exporting Unknown Wiki List... --------------------')
match group_by:
    case 'Owner' | 'Category':
        path_to_export = UnknownWikiListExporterForLLM(group_by = group_by).run()

        match language:
            case 'English' | 'Japanese':
                path_to_export = UnknownWikiListExporterForLLM(group_by = group_by, language = language).run()
    case _:
        path_to_export = UnknownWikiListExporterForLLM().run()
print()
print("Check it out result on '#{path_to_export}' !!")
print()
print('-------------------- Done Exporting Unknown Wiki List 🎉 --------------------')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
