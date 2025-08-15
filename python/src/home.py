import sys
import os
import re
sys.path.append('./src')

from application import Application

HOME_URL = f'https://github.com/{os.environ.get('ORGANISATION_NAME', 'hayat01sh1da')}/github-wiki-organisers/wiki'

class Home(Application):
    def __init__(self, base_path = os.path.join('..', '..'), group_by = 'Owner', language = 'English', home_overflow = False):
        super().__init__(base_path, group_by, language, home_overflow)
        self.base_owner_url = f'https://github.com/orgs/{os.environ.get('ORGANISATION_NAME', 'hayat01sh1da')}/teams/'
        self.home_passage   = self.__home_passage__()

    def run(self):
        self.__write_home_passage__()
        return HOME_URL

    # private

    # @return [str]
    def __path_to_home_template__(self):
        return os.path.join('..', 'home_template', self.group_by.lower(), f'{self.language.lower()}.md')

    # @return [list<str>]
    def __home_passage__(self):
        with open(self.__path_to_home_template__()) as f:
            return f.read() + '\n'

    # @return [str]
    def __write_home_passage__(self):
        if self.home_overflow:
            path_to_wikis_by_owners = os.path.join(self.base_path, 'wikis_by_owners')
            if not os.path.exists(self.base_path):
                os.makedirs(path_to_wikis_by_owners)

            for namespace, wikis in self.owned_wiki_maps.items():
                home_passage  = ''
                home_passage += f'## [{namespace}]({self.base_owner_url + re.sub(r'@', '', namespace)})\n'
                home_passage += '\n'
                for wiki in wikis:
                    home_passage += f'- [[{re.sub(r'\.md', '', wiki)}]]\n'
                home_passage += '\n'
                with open(path_to_wikis_by_owners, 'w') as f:
                    f.write(home_passage.rstrip() + '\n')

            for namespace, wikis in self.plain_wiki_maps.items():
                home_passage  = ''
                home_passage += f'## {namespace}\n'
                home_passage += '\n'
                for wiki in wikis:
                    home_passage += f'- [[{re.sub(r'\.md', '', wiki)}]]\n'
                home_passage += '\n'
                with open(path_to_wikis_by_owners, 'w') as f:
                    f.write(home_passage.rstrip() + '\n')

            for namespace in self.owned_wiki_maps.keys():
                self.home_passage += f'[[{namespace}]]'

            for namespace in self.plain_wiki_maps.keys():
                self.home_passage += f'[[{namespace}]]'

        else:
            for namespace, wikis in self.owned_wiki_maps.items():
                self.home_passage += f'## [{namespace}]({self.base_owner_url + re.sub(r'@', '', namespace)})\n'
                self.home_passage += '\n'
                for wiki in wikis:
                    self.home_passage += f'- [[{re.sub(r'\.md', '', wiki)}]]\n'
                self.home_passage += '\n'

            for namespace, wikis in self.plain_wiki_maps.items():
                self.home_passage += f'## {namespace}\n'
                self.home_passage += '\n'
                for wiki in wikis:
                    self.home_passage += f'- [[{re.sub(r'\.md', '', wiki)}]]\n'
                self.home_passage += '\n'

            with open(self.path_to_home, 'w') as f:
                f.write(self.home_passage.rstrip() + '\n')
