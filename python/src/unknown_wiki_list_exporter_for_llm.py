import sys
import os
sys.path.append('./src')
from application import Application

class UnknownWikiListExporterForLLM(Application):
    def __init__(self, base_path = os.path.join('..', '..'), group_by = '-o', language = '-en'):
        super().__init__(base_path, group_by, language)
        self.path_to_export               = os.path.join(self.base_path, 'unknown_wiki_list_for_llm.txt')
        self.unknown_wiki_list_for_llm = ''.join(sorted(self.__unknown_wiki_list_for_llm__()))

    def run(self):
        with open(self.path_to_export, 'w') as f:
            f.write(self.unknown_wiki_list_for_llm.rstrip() + '\n')

        return self.path_to_export

    # private

    # @return [str]
    def __target_namespace__(self):
        match self.group_by:
            case '-o' | '--owner':
                match self.language:
                    case '-en':
                        return 'Unknown Owner nor Necessity'
                    case '-ja':
                        return 'Ownerチーム・要or不要が不明なページ群'
            case '-c' | '--category':
                match self.language:
                    case '-en':
                        return 'Uncategorised'
                    case '-ja':
                        return 'Category記載なし'

    # @return [list<str>]
    def __unknown_wiki_list_for_llm__(self):
        unknown_wiki_list_for_llm = []

        for namespace, wikis in self.plain_wiki_maps.items():
            if namespace == self.__target_namespace__():
                for wiki in wikis:
                    unknown_wiki_list_for_llm.append(f'{wiki}\n')

        return unknown_wiki_list_for_llm
