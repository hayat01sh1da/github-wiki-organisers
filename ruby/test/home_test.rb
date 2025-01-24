require_relative './application_test'
require_relative '../src/home'

class HomeTest < ApplicationTest
  def setup
    super
    Home.run(base_path:)
    path_to_home = File.join(base_path, 'Home.md')
    @home        = IO.read(path_to_home)
  end

  def test_self_run
    assert_equal(home, home_passage.join)
  end

  private

  attr_reader :home

  def home_passage
    passage  = []
    passage << "このページは Owner チームごとに Wiki をグルーピングして一覧化しています。\n\n"
    passage << "## Wiki ページの運用ルール\n\n"
    passage << "Ownership をどのチームが持つのかが不明だと、責任の所在が不明瞭になり、保守性の悪化に伴うノイズの増加と検索性の悪化が発生します。  \n"
    passage << "治安維持のため、各ページの冒頭に `Owner: {オーナーチーム名}` を明記して頂きますようよろしくお願いします。  \n"
    passage << "なお、Home・Sidebar は専用のスクリプトで自動更新しますので編集は不要です。\n\n"
    passage << "## [@test-owner](https://github.com/orgs/quipper/teams/test-owner)\n\n"
    passage << "- [[Owner記名ありページ]]\n\n"
    passage << "## Ownerチームが不明だが必要なページ群\n\n"
    passage << "- [[Ownerチームが不明だが必要なページ]]\n\n"
    passage << "## Ownerチーム・要or不要が不明なページ群\n\n"
    passage << "- [[Ownerチーム・要or不要が不明なページ]]\n\n"
    passage << "## Owner記名なし\n\n"
    passage << "- [[Owner記名なしページ1]]\n"
    passage << "- [[Owner記名なしページ2]]\n"
  end
end
