import sys
import os
import re
sys.path.append('./src')
from application import Application

HOME_URL = f'https://github.com/{os.environ.get('USERNAME', 'hayat01sh1da')}/github-wiki-organisers/wiki'

class Home(Application):
    def __init__(self, base_path, genre):
        super().__init__(base_path, genre)
        self.base_owner_url = f'https://github.com/orgs/{os.environ.get('USERNAME', 'hayat01sh1da')}/teams/'
        self.home_passage = ''

    def run(self):
        self.__write_home_template__()
        self.__update_home_template__()
        with open(self.path_to_home, 'w') as f:
            f.write(self.home_passage.rstrip() + '\n')
        return HOME_URL

    # private

    # @return [str]
    def __write_home_template__(self):
        match self.genre:
            case '-o' | '--owner':
                self.home_passage += 'このページは Owner チームごとに Wiki をグルーピングして一覧化しています。\n\n'
                self.home_passage += '## Wiki ページの運用ルール\n\n'
                self.home_passage += 'Ownership をどのチームが持つのかが不明だと、責任の所在が不明瞭になり、保守性の悪化に伴うノイズの増加と検索性の悪化が発生します。  \n'
                self.home_passage += '治安維持のため、各ページの冒頭に `Owner: {オーナーチーム名}` を明記して頂きますようよろしくお願いします。  \n'
            case '-c' | '--category':
                self.home_passage += 'このページは Category ごとに Wiki をグルーピングして一覧化しています。\n\n'
                self.home_passage += '## Wiki ページの運用ルール\n\n'
                self.home_passage += 'Category が不明だと、保守性と検索性の悪化が発生します。  \n'
                self.home_passage += '治安維持のため、各ページの冒頭に `Category: {カテゴリー名}` を明記して頂きますようよろしくお願いします。  \n'

        self.home_passage += 'なお、Home・Sidebar は専用のスクリプトで自動更新しますので編集は不要です。\n\n'

    # @return [str]
    def __update_home_template__(self):
        for namespace, wikis in self.owned_wiki_maps.items():
            self.home_passage += f'## [{namespace}]({self.base_owner_url + re.sub(r'@', '', namespace)})\n\n'
            self.home_passage += '<details><summary>Wiki 一覧</summary>\n\n'
            for wiki in wikis:
                self.home_passage += f'- [[{re.sub(r'\.md', '', wiki)}]]\n'
            self.home_passage += '\n</details>\n'
            self.home_passage += '\n'

        for namespace, wikis in self.plain_wiki_maps.items():
            self.home_passage += f'## {namespace}\n\n'
            self.home_passage += '<details><summary>Wiki 一覧</summary>\n\n'
            for wiki in wikis:
                self.home_passage += f'- [[{re.sub(r'\.md', '', wiki)}]]\n'
            self.home_passage += '\n</details>\n'
            self.home_passage += '\n'
