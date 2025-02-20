import sys
import os
sys.path.append('./src')
from application import Application

NAMESPACE_LIST = (
    'Ownerチームが不明だが必要なページ群',
    'Ownerチーム・要or不要が不明なページ群',
    'Owner記名なし'
)

class UnknownWikiCountListExporter(Application):
    def __init__(self, base_path = os.path.join('..', '..')):
        super().__init__(base_path)
        self.path_to_export          = os.path.join(self.base_path, 'unowned_wiki_count_list_by_namespace.txt')
        self.count_list_by_namespace = ''.join(sorted(self.__count_list_by_namespace__()))

    def run(self):
        with open(self.path_to_export, 'w') as f:
            f.write(self.count_list_by_namespace.rstrip() + '\n')

        return self.count_list_by_namespace.rstrip() + '\n', self.path_to_export

    # private

    # @return [list<str>]
    def __count_list_by_namespace__(self):
        count_list_by_namespace = []

        for namespace in (NAMESPACE_LIST - self.unowned_wiki_maps.keys()):
            count_list_by_namespace.append(
                '{namespace}: 0件\n'.format(namespace=namespace))

        for namespace, wikis in self.unowned_wiki_maps.items():
            count_list_by_namespace.append('{namespace}: {count}件\n'.format(namespace = namespace, count = len(wikis)))

        return count_list_by_namespace
