import os
import glob
import re

class Application:
    def __init__(self, base_path = os.path.join('..', '..')):
        self.base_path           = base_path
        self.path_to_home        = os.path.join(base_path, 'Home.md')
        self.path_to_sidebar     = os.path.join(base_path, '_Sidebar.md')
        self.target_paths        = sorted(glob.glob(os.path.join(base_path, '**', '*.md'), recursive = True))
        self.owner_and_wiki_maps = {}

    def run(self):
        raise NotImplementedError('This method must be implemented in each subclass.')

    # private

    # @return [str]
    def __target_paths__(self):
        for target_path in self.target_paths:
            if target_path == self.path_to_home or target_path == self.path_to_sidebar or re.search(r'github\-wiki\-organisers', target_path):
                self.target_paths.remove(target_path)
            else:
                continue

    # @return [dict<str => list<str>>]
    def __owner_and_wiki_maps__(self):
        self.__target_paths__()
        for target_path in self.target_paths:
            with open(target_path) as f:
                wiki = os.path.basename(target_path)

                _ownership_declaration = f.readlines()
                if _ownership_declaration != [] and re.search(r'[Oo]wner', _ownership_declaration[0]):
                    ownership_declaration = re.sub('\n', '', _ownership_declaration[0])
                    owner                 = re.sub(r'Owner:\s?', '', ownership_declaration)
                else:
                    owner = 'Owner記名なし'

                try:
                    self.owner_and_wiki_maps[owner]
                except KeyError:
                    self.owner_and_wiki_maps[owner] = []

                self.owner_and_wiki_maps[owner].append(wiki)

        self.owner_and_wiki_maps = dict(sorted(self.owner_and_wiki_maps.items()))
