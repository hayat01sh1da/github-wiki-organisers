require_relative './application_test'
require_relative '../src/home'

class HomeTest < ApplicationTest
  def setup(genre: '-o')
    super(genre:)
    Home.run(base_path:, genre:)
    @path_to_home = File.join(base_path, 'Home.md')
    @home         = File.read(path_to_home)
  end

  private

  attr_reader :path_to_home, :home
end

class OwnedHomeTest < HomeTest
  def test_self_run
    assert_equal(home_passage.join, home)
  end

  private

  def home_passage
    [
      "このページは Owner チームごとに Wiki をグルーピングして一覧化しています。\n\n",
      "## Wiki ページの運用ルール\n\n",
      "Ownership をどのチームが持つのかが不明だと、責任の所在が不明瞭になり、保守性の悪化に伴うノイズの増加と検索性の悪化が発生します。  \n",
      "治安維持のため、各ページの冒頭に `Owner: {オーナーチーム名}` を明記して頂きますようよろしくお願いします。  \n",
      "なお、Home・Sidebar は専用の定期実行ジョブで自動更新しますので編集は不要です。\n\n",
      "## [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n\n",
      "- [[Owner記名ありページ]]\n",
      "\n",
      "## Ownerチームが不明だが必要なページ群\n\n",
      "- [[Ownerチームが不明だが必要なページ]]\n",
      "\n",
      "## Ownerチーム・要or不要が不明なページ群\n\n",
      "- [[Ownerチーム・要or不要が不明なページ]]\n",
      "\n",
      "## Owner記名なし\n\n",
      "- [[Owner記名なしページ1]]\n",
      "- [[Owner記名なしページ2]]\n"
    ]
  end
end

class PlainHomeTest < HomeTest
  def setup
    super(genre: '-c')
  end

  def test_self_run
    assert_equal(home_passage.join, home)
  end

  private

  def home_passage
    [
      "このページは Category ごとに Wiki をグルーピングして一覧化しています。\n\n",
      "## Wiki ページの運用ルール\n\n",
      "Category が不明だと、保守性と検索性の悪化が発生します。  \n",
      "治安維持のため、各ページの冒頭に `Category: {カテゴリー名}` を明記して頂きますようよろしくお願いします。  \n",
      "なお、Home・Sidebar は専用の定期実行ジョブで自動更新しますので編集は不要です。\n\n",
      "## test-category\n\n",
      "- [[Category記載ありページ]]\n",
      "\n",
      "## Category記載なし\n\n",
      "- [[Category記載なしページ1]]\n",
      "- [[Category記載なしページ2]]\n"
    ]
  end
end
