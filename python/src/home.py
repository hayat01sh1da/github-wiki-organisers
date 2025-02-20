import sys
import os
import re
sys.path.append('./src')
from application import Application

HOME_URL = 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki'

class Home(Application):
    def __init__(self, base_path = os.path.join('..', '..')):
        super().__init__(base_path)
        self.base_owner_url = 'https://github.com/orgs/hayat01sh1da/teams/'
        self.home_passage   = self.__write_home_template__()

    def run(self):
        with open(self.path_to_home, 'w') as f:
            f.write(self.home_passage.rstrip() + '\n')
        return HOME_URL

    # private

    # @return [str]
    def __write_home_template__(self):
        home_passage  = 'このページは Owner チームごとに Wiki をグルーピングして一覧化しています。\n\n'
        home_passage += '## Wiki ページの運用ルール\n\n'
        home_passage += 'Ownership をどのチームが持つのかが不明だと、責任の所在が不明瞭になり、保守性の悪化に伴うノイズの増加と検索性の悪化が発生します。  \n'
        home_passage += '治安維持のため、各ページの冒頭に `Owner: {オーナーチーム名}` を明記して頂きますようよろしくお願いします。  \n'
        home_passage += 'なお、Home・Sidebar は専用のスクリプトで自動更新しますので編集は不要です。\n\n'

        for owner, wikis in self.owned_wiki_maps.items():
            home_passage += '## [{owner}]({owner_url})\n\n'.format(owner = owner, owner_url = self.base_owner_url + re.sub(r'@', '', owner))
            for wiki in wikis:
                home_passage += '- [[{wiki}]]\n'.format(wiki = re.sub(r'\.md', '', wiki))
            home_passage += '\n'

        for namespace, wikis in self.unowned_wiki_maps.items():
            home_passage += '## {namespace}\n\n'.format(namespace = namespace)
            for wiki in wikis:
                home_passage += '- [[{wiki}]]\n'.format(wiki = re.sub(r'\.md', '', wiki))
            home_passage += '\n'

        return home_passage
