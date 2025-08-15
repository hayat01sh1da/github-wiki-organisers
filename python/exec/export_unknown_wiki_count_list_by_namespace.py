import sys
import os
import shutil
import glob
sys.path.append('./src')

from unknown_wiki_count_list_exporter import UnknownWikiCountListExporter

_, group_by, language, *_ = sys.argv

print('-------------------- Exporting Unknown Wiki Count List... --------------------')
match group_by:
    case '-o' | '--owner' | '-c' | '--category':
        count_list_by_namespace, path_to_export = UnknownWikiCountListExporter(group_by = group_by).run()

        match language:
            case '-en' | '-ja':
                count_list_by_namespace, path_to_export = UnknownWikiCountListExporter(group_by = group_by, language = language).run()
    case _:
        count_list_by_namespace, path_to_export = UnknownWikiCountListExporter().run()
print()
print('Here is the result:')
print()
print('---------------------------------------')
print(count_list_by_namespace.rstrip())
print('---------------------------------------')
print()
print(f"Check it out result on '{path_to_export}' !!")
print()
print('-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
