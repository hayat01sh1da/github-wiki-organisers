import sys
import os
sys.path.append('./src')
from application import Application

class UnknownWikiListExporterForLLM(Application):
    def __init__(self, base_path = os.path.join('..', '..'), group_by = 'Owner', language = 'English'):
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
            case 'Owner':
                match self.language:
                    case 'English':
                        return 'Unknown Owner nor Necessity'
                    case 'Japanese':
                        return 'Ownerチーム・要or不要が不明なページ群'
            case 'Category':
                match self.language:
                    case 'English':
                        return 'Uncategorised'
                    case 'Japanese':
                        return 'Category記載なし'

    # @return [list<str>]
    def __unknown_wiki_list_for_llm__(self):
        unknown_wiki_list_for_llm = []

        for namespace, wikis in self.plain_wiki_maps.items():
            if namespace == self.__target_namespace__():
                for wiki in wikis:
                    unknown_wiki_list_for_llm.append(f'{wiki}\n')

        return unknown_wiki_list_for_llm
