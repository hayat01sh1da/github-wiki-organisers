import sys
import os
sys.path.append('./src')

from application import Application

class UnknownWikiCountListExporter(Application):
    def __init__(self, base_path = os.path.join('..', '..'), group_by = '-o', language = '-en'):
        super().__init__(base_path, group_by, language)
        self.path_to_export          = os.path.join(self.base_path, 'unknown_wiki_count_list_by_namespace.txt')
        self.count_list_by_namespace = ''.join(sorted(self.__count_list_by_namespace__()))

    def run(self):
        with open(self.path_to_export, 'w') as f:
            f.write(self.count_list_by_namespace.rstrip() + '\n')

        return self.count_list_by_namespace.rstrip() + '\n', self.path_to_export

    # private

    # @return [list<str>]
    def __namespace_list__(self):
        match self.group_by:
            case '-o' | '--owner':
                match self.language:
                    case '-en':
                        return [
                            'Unowned but Necessary',
                            'Unknown Owner nor Necessity',
                            'Unowned'
                        ]
                    case '-ja':
                        return [
                            'Ownerチームが不明だが必要なページ群',
                            'Ownerチーム・要or不要が不明なページ群',
                            'Owner記名なし'
                        ]
            case '-c' | '--category':
                match self.language:
                    case '-en':
                        return [
                            'Uncategorised'
                        ]
                    case '-ja':
                        return [
                            'Category記載なし'
                        ]

    # @return [list<str>]
    def __count_list_by_namespace__(self):
        filtered_count_list_by_namespace = {}
        count_list_by_namespace          = []

        for namespace, wikis in self.plain_wiki_maps.items():
            if namespace in self.__namespace_list__():
                filtered_count_list_by_namespace[namespace] = wikis

        for namespace in (self.__namespace_list__() - filtered_count_list_by_namespace.keys()):
            count_list_by_namespace.append(f'{namespace}: 0\n')

        for namespace, wikis in filtered_count_list_by_namespace.items():
            count_list_by_namespace.append(f'{namespace}: {len(wikis)}\n')

        return count_list_by_namespace
