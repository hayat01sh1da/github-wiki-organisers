import sys
import os
import re
sys.path.append('./src')
from application import Application

class Sidebar(Application):
    def __init__(self, base_path = os.path.join('..', '..')):
        super().__init__(base_path)
        self.base_owner_url    = 'https://github.com/orgs/hayat01sh1da/teams/'
        self.wiki_list         = ''
        self.owned_wiki_maps   = {}
        self.unowned_wiki_maps = {}

    def run(self):
        self.__target_paths__()
        self.__owner_and_wiki_maps__()
        self.__filter_owners__()
        self.__update_wiki_list__()
        with open(self.path_to_sidebar, 'w') as f:
            f.write(self.wiki_list)

    # private

    # @return None
    def __filter_owners__(self):
        for namespace, wikis in self.owner_and_wiki_maps.items():
            if re.search(r'@', namespace):
                self.owned_wiki_maps[namespace] = wikis
            else:
                self.unowned_wiki_maps[namespace] = wikis

    # @return [str]
    def __update_wiki_list__(self):
        for owner, wikis in self.owned_wiki_maps.items():
            self.wiki_list += '- [{owner}]({owner_url})\n'.format(owner = owner, owner_url = self.base_owner_url + re.sub(r'@', '', owner))
            for wiki in wikis:
                self.wiki_list += '  - [[{wiki}]]\n'.format(wiki = re.sub(r'\.md', '', wiki))

        for namespace, wikis in self.unowned_wiki_maps.items():
            self.wiki_list += '- {namespace}\n'.format(namespace = namespace)
            for wiki in wikis:
                self.wiki_list += '  - [[{wiki}]]\n'.format(wiki = re.sub(r'\.md', '', wiki))
