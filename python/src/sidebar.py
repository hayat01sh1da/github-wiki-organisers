import sys
import os
import re
sys.path.append('./src')
from application import Application

class Sidebar(Application):
    def __init__(self, base_path = os.path.join('..', '..')):
        super().__init__(base_path)
        self.base_owner_url = 'https://github.com/orgs/{user_name}/teams/'.format(user_name = os.environ.get('USERNAME', 'hayat01sh1da'))
        self.wiki_list      = self.__write_wiki_list__()

    def run(self):
        with open(self.path_to_sidebar, 'w') as f:
            f.write(self.wiki_list)

    # private

    # @return [str]
    def __write_wiki_list__(self):
        wiki_list = ''

        for owner, wikis in self.owned_wiki_maps.items():
            wiki_list += '- [{owner}]({owner_url})\n'.format(owner = owner, owner_url = self.base_owner_url + re.sub(r'@', '', owner))
            for wiki in wikis:
                wiki_list += '  - [[{wiki}]]\n'.format(wiki = re.sub(r'\.md', '', wiki))

        for namespace, wikis in self.plain_wiki_maps.items():
            wiki_list += '- {namespace}\n'.format(namespace = namespace)
            for wiki in wikis:
                wiki_list += '  - [[{wiki}]]\n'.format(wiki = re.sub(r'\.md', '', wiki))

        return wiki_list
