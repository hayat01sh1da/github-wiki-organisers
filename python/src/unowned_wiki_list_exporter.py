import sys
import os
sys.path.append('./src')
from application import Application

NAMESPACE_LIST = (
    'Ownerチームが不明だが必要なページ群',
    'Ownerチーム・要or不要が不明なページ群',
    'Owner記名なし'
)

class UnknownWikiListExporter(Application):
    def __init__(self, base_path = os.path.join('..', '..')):
        super().__init__(base_path)
        self.path_to_export           = os.path.join(self.base_path, 'unowned_wiki_count_list_by_namespace.txt')
        self.count_lists_by_namespace = []

    def run(self):
        self.__target_paths__()
        self.__owner_and_wiki_maps__()
        self.__filter_owners__()
        self.__missing_count_lists_by_namespace__()
        self.__count_lists_by_namespace__()
        self.count_lists_by_namespace = ''.join(sorted(self.count_lists_by_namespace))

        with open(self.path_to_export, 'w') as f:
            f.write(self.count_lists_by_namespace.rstrip() + '\n')

        return self.count_lists_by_namespace.rstrip() + '\n', self.path_to_export

    # private

    # @return [list<str>]
    def __missing_count_lists_by_namespace__(self):
        for namespace in (NAMESPACE_LIST - self.unowned_wiki_maps.keys()):
            self.count_lists_by_namespace.append('{namespace}: 0件\n'.format(namespace = namespace))

    # @return [list<str>]
    def __count_lists_by_namespace__(self):
        for namespace, wikis in self.unowned_wiki_maps.items():
            self.count_lists_by_namespace.append('{namespace}: {count}件\n'.format(namespace = namespace, count = len(wikis)))
