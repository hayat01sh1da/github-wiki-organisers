import os
import glob
import re
from collections import defaultdict

class Application:
    def __init__(self, base_path = os.path.join('..', '..'), genre = '-o'):
        self.base_path                             = base_path
        self.genre                                 = genre
        self.path_to_home                          = os.path.join(base_path, 'Home.md')
        self.path_to_sidebar                       = os.path.join(base_path, '_Sidebar.md')
        self.target_paths                          = self.__target_paths__()
        self.wiki_maps_with_namespace              = self.__wiki_maps_with_namespace__()
        self.owned_wiki_maps, self.plain_wiki_maps = self.__filter_namespace__()

    def validate(self):
        if self.genre not in ['-o', '--owner', '-c', '--category']:
            raise ValueError(f'Unknown genre: `{self.genre}`')

    def run(self):
        raise NotImplementedError('This method must be implemented in each subclass.')

    # private

    # @return [str]
    def __target_paths__(self):
        target_paths = sorted(glob.glob(os.path.join(self.base_path, '**', '*.md'), recursive = True))

        for target_path in target_paths:
            match target_path:
                case self.path_to_home | self.path_to_sidebar:
                    target_paths.remove(target_path)
                case _:
                    if re.search(r'github\-wiki\-organisers', target_path):
                        target_paths.remove(target_path)
                    else:
                        continue

        return target_paths

    # @return [regex]
    def __target_regexp__(self):
        match self.genre:
            case '-o' | '--owner':
                return re.compile(r'[Oo]wner:\s?')
            case '-c' | '--category':
                return re.compile(r'[Cc]ategory:\s?')
            case _:
                raise ValueError(f'Unknown genre: `{self.genre}`')

    # @return [str]
    def __no_declaration__(self):
        match self.genre:
            case '-o' | '--owner':
                return 'Owner記名なし'
            case '-c' | '--category':
                return 'Category記載なし'
            case _:
                raise ValueError(f'Unknown genre: `{self.genre}`')

    # @return [dict<str => list<str>>]
    def __filter_namespace__(self):
        owned_wiki_maps = {}
        plain_wiki_maps = {}

        for namespace, wikis in self.wiki_maps_with_namespace.items():
            if re.search(r'@', namespace):
                owned_wiki_maps[namespace] = wikis
            else:
                plain_wiki_maps[namespace] = wikis

        return owned_wiki_maps, plain_wiki_maps

    # @return [dict<str => list<str>>]
    def __wiki_maps_with_namespace__(self):
        hash                     = defaultdict(list)
        uncategrised_wiki_maps   = defaultdict(list)
        wiki_maps_with_namespace = defaultdict(list)

        for target_path in self.target_paths:
            with open(target_path) as f:
                wiki                   = os.path.basename(target_path)
                _namespace_declaration = f.readlines()

                if _namespace_declaration != [] and re.search(self.__target_regexp__(), _namespace_declaration[0]):
                    namespace_declaration  = re.sub('\n', '', _namespace_declaration[0])
                    namespace              = re.sub(self.__target_regexp__(), '', namespace_declaration)
                else:
                    namespace = self.__no_declaration__()

                if namespace == self.__no_declaration__():
                    uncategrised_wiki_maps[namespace].append(wiki)
                else:
                    hash[namespace].append(wiki)

        wiki_maps_with_namespace = dict(sorted(hash.items()))
        wiki_maps_with_namespace.update(uncategrised_wiki_maps)

        return wiki_maps_with_namespace
