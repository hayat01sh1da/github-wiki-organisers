import os
import glob
import re

class Application:
        self.base_path                             = base_path
        self.path_to_home                          = os.path.join(base_path, 'Home.md')
        self.path_to_sidebar                       = os.path.join(base_path, '_Sidebar.md')
        self.target_paths                          = self.__target_paths__()
        self.wiki_maps_with_namespace              = self.__wiki_maps_with_namespace__()
        self.owned_wiki_maps, self.plain_wiki_maps = self.__filter_owners__()

    def run(self):
        raise NotImplementedError('This method must be implemented in each subclass.')

    # private

    # @return [str]
    def __target_paths__(self):
        target_paths = sorted(glob.glob(os.path.join(self.base_path, '**', '*.md'), recursive = True))

        for target_path in target_paths:
            if target_path == self.path_to_home or target_path == self.path_to_sidebar or re.search(r'github\-wiki\-organisers', target_path):
                target_paths.remove(target_path)
            else:
                continue

        return target_paths

    # @return [dict<str => list<str>>]
    def __wiki_maps_with_namespace__(self):
        wiki_maps_with_namespace = {}

        for target_path in self.target_paths:
            with open(target_path) as f:
                wiki = os.path.basename(target_path)

                _ownership_declaration = f.readlines()
                if _ownership_declaration != [] and re.search(r'[Oo]wner', _ownership_declaration[0]):
                    ownership_declaration = re.sub('\n', '', _ownership_declaration[0])
                    owner                 = re.sub(r'[Oo]wner:\s?', '', ownership_declaration)
                else:
                    owner = 'Owner記名なし'

                try:
                    wiki_maps_with_namespace[owner]
                except KeyError:
                    wiki_maps_with_namespace[owner] = []

                wiki_maps_with_namespace[owner].append(wiki)

        return dict(sorted(wiki_maps_with_namespace.items()))

    # @return [dict<str => list<str>>]
    def __filter_owners__(self):
        owned_wiki_maps = {}
        plain_wiki_maps = {}

        for namespace, wikis in self.wiki_maps_with_namespace.items():
            if re.search(r'@', namespace):
                owned_wiki_maps[namespace] = wikis
            else:
                plain_wiki_maps[namespace] = wikis

        return owned_wiki_maps, plain_wiki_maps
