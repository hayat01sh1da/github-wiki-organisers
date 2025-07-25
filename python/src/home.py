import sys
import os
import re
sys.path.append('./src')

from application import Application

HOME_URL = f'https://github.com/{os.environ.get('USERNAME', 'hayat01sh1da')}/github-wiki-organisers/wiki'

class Home(Application):
    def __init__(self, base_path = os.path.join('..', '..'), genre = '-o', language = '-en'):
        super().__init__(base_path, genre, language)
        self.base_owner_url = f'https://github.com/orgs/{os.environ.get('USERNAME', 'hayat01sh1da')}/teams/'
        self.home_passage   = self.__home_passage__()

    def run(self):
        self.__update_home_template__()
        with open(self.path_to_home, 'w') as f:
            f.write(self.home_passage.rstrip() + '\n')
        return HOME_URL

    # private

    # @return [str]
    def __template_genre__(self):
        match self.genre:
            case '-o' | '--owner':
                return 'owner'
            case '-c' | '--category':
                return 'category'

    # @return [str]
    def __path_to_home_template__(self):
        return os.path.join('..', 'home_template', self.__template_genre__(), f'{ re.sub(r'^-', '', self.language)}.md')

    # @return [list<str>]
    def __home_passage__(self):
        with open(self.__path_to_home_template__()) as f:
            return f.read() + '\n'

    # @return [str]
    def __update_home_template__(self):
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
