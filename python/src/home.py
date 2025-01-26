import sys
import os
import re
sys.path.append('./src')
from application import Application

HOME_URL = 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki'

class Home(Application):

    def __init__(self, base_path = os.path.join('..', '..')):
        super().__init__(base_path)
        self.base_owner_url    = 'https://github.com/orgs/quipper/teams/'
        self.home_passage      = ''
        self.owned_wiki_maps   = {}
        self.unowned_wiki_maps = {}

    def run(self):
        self.__target_paths__()
        self.__owner_and_wiki_maps__()
        self.__filter_owners__()
        self.__write_home_template__()
        self.__update_home_passage__()
        with open(self.path_to_home, 'w') as f:
            f.write(self.home_passage.rstrip() + '\n')
        return HOME_URL

    # private

    # @return None
    def __filter_owners__(self):
        for namespace, wikis in self.owner_and_wiki_maps.items():
            if re.search(r'@', namespace):
                self.owned_wiki_maps[namespace] = wikis
            else:
                self.unowned_wiki_maps[namespace] = wikis

    # @return [str]
    def __write_home_template__(self):
        self.home_passage += 'このページは Owner チームごとに Wiki をグルーピングして一覧化しています。\n\n'
        self.home_passage += '## Wiki ページの運用ルール\n\n'
        self.home_passage += 'Ownership をどのチームが持つのかが不明だと、責任の所在が不明瞭になり、保守性の悪化に伴うノイズの増加と検索性の悪化が発生します。  \n'
        self.home_passage += '治安維持のため、各ページの冒頭に `Owner: {オーナーチーム名}` を明記して頂きますようよろしくお願いします。  \n'
        self.home_passage += 'なお、Home・Sidebar は専用のスクリプトで自動更新しますので編集は不要です。\n\n'

    # @return [str]
    def __update_home_passage__(self):
        for owner, wikis in self.owned_wiki_maps.items():
            self.home_passage += '## [{owner}]({owner_url})\n\n'.format(owner = owner, owner_url = self.base_owner_url + re.sub(r'@', '', owner))
            for wiki in wikis:
                self.home_passage += '- [[{wiki}]]\n'.format(wiki = re.sub(r'\.md', '', wiki))
            self.home_passage += '\n'

        for namespace, wikis in self.unowned_wiki_maps.items():
            self.home_passage += '## {namespace}\n\n'.format(namespace = namespace)
            for wiki in wikis:
                self.home_passage += '- [[{wiki}]]\n'.format(wiki = re.sub(r'\.md', '', wiki))
            self.home_passage += '\n'
