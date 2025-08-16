import os
import glob
import re
from collections import defaultdict

class Application:
    def __init__(self, base_path = os.path.join('..', '..'), group_by = 'Owner', language = 'English', home_overflow = False):
        self.__validate__(group_by = group_by, language = language, home_overflow = home_overflow)
        self.base_path                             = base_path
        self.group_by                              = group_by
        self.language                              = language
        self.home_overflow                         = home_overflow
        self.path_to_home                          = os.path.join(base_path, 'Home.md')
        self.path_to_sidebar                       = os.path.join(base_path, '_Sidebar.md')
        self.target_paths                          = self.__target_paths__()
        self.wiki_maps_with_namespace              = self.__wiki_maps_with_namespace__()
        self.owned_wiki_maps, self.plain_wiki_maps = self.__filter_namespace__()

    def run(self):
        raise NotImplementedError('This method must be implemented in each subclass.')

    # private

    # @raises [ValueError]
    def __validate__(self, group_by, language, home_overflow):
        if group_by not in ['Owner', 'Category']:
            raise ValueError(f'Invalid group_by: `{group_by}`')
        if language not in ['English', 'Japanese']:
            raise ValueError(f'Invalid language: `{language}`')
        if home_overflow not in [True, False]:
            raise ValueError(f'Invalid home_overflow: `{home_overflow}` must be boolean')

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
        match self.group_by:
            case 'Owner':
                return re.compile(r'[Oo]wner:\s?')
            case 'Category':
                return re.compile(r'[Cc]ategory:\s?')

    # @return [str]
    def __no_declaration__(self):
        match self.group_by:
            case 'Owner':
                match self.language:
                    case 'English':
                        return 'Unowned'
                    case 'Japanese':
                        return 'Owner記名なし'
            case 'Category':
                match self.language:
                    case 'English':
                        return 'Uncategorised'
                    case 'Japanese':
                        return 'Category記載なし'

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
