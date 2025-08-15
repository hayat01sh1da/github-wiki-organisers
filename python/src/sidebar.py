import sys
import os
import re
sys.path.append('./src')

from application import Application

class Sidebar(Application):
    def __init__(self, base_path = os.path.join('..', '..'), group_by = 'Owner', language = 'English'):
        super().__init__(base_path, group_by, language)
        self.base_owner_url = f'https://github.com/orgs/{os.environ.get('ORGANISATION_NAME', 'hayat01sh1da')}/teams/'
        self.wiki_list      = self.__write_wiki_list__()

    def run(self):
        with open(self.path_to_sidebar, 'w') as f:
            f.write(self.wiki_list)

    # private

    # @return [str]
    def __write_wiki_list__(self):
        wiki_list = ''

        for namespace, wikis in self.owned_wiki_maps.items():
            wiki_list += f'- [{namespace}]({self.base_owner_url + re.sub(r'@', '', namespace)})\n'
            for wiki in wikis:
                wiki_list += f'  - [[{re.sub(r'\.md', '', wiki)}]]\n'

        for namespace, wikis in self.plain_wiki_maps.items():
            wiki_list += f'- {namespace}\n'
            for wiki in wikis:
                wiki_list += f'  - [[{re.sub(r'\.md', '', wiki)}]]\n'

        return wiki_list
