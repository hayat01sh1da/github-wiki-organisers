import sys
import os
import shutil
import glob
sys.path.append('./src')

from unknown_wiki_list_exporter_for_llm import UnknownWikiListExporterForLLM

_, genre, language, *_ = sys.argv

print('-------------------- Exporting Unknown Wiki List... --------------------')
match genre:
    case '-o' | '--owner' | '-c' | '--category':
        path_to_export = UnknownWikiListExporterForLLM(genre = genre).run()

        match language:
            case '-en' | '-ja':
                path_to_export = UnknownWikiListExporterForLLM(genre = genre, language = language).run()
    case _:
        path_to_export = UnknownWikiListExporterForLLM().run()
print()
print("Check it out result on '#{path_to_export}' !!")
print()
print('-------------------- Done Exporting Unknown Wiki List 🎉 --------------------')

for pycache in glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True):
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
