require_relative './application_test'
require_relative '../src/home'

class HomeTest < ApplicationTest
  def setup(genre: '-o', template_lang: 'ja')
    super(genre:)
    Home.run(base_path:, genre:, template_lang:)
    @path_to_home = File.join(base_path, 'Home.md')
    @home         = File.read(path_to_home)
  end

  def test_validate!
    error = assert_raises ArgumentError do
      Home.new(base_path:, genre: '-o', template_lang: 'spa').validate!
    end
    assert_equal('Unknown template_lang: `spa`', error.message)
  end

  private

  attr_reader :path_to_home, :home
end

module Japanese
  class OwnedHomeTest < HomeTest
    def test_self_run
      assert_equal(home_passage.join, home)
    end

    private

    def home_passage
      [
        "## Wiki ページの運用ルール\n",
        "\n",
        "このページは Owner チームごとに Wiki をグルーピングして一覧化しています。\n",
        "\n",
        "Ownership をどのチームが持つのかが不明だと、責任の所在が不明瞭になり、保守性の悪化に伴うノイズの増加と検索性の悪化が発生します。  \n",
        "治安維持のため、各ページの冒頭に `Owner: @オーナーチーム` を明記して頂きますようよろしくお願いします。\n",
        "\n",
        "なお、Home・Sidebar は専用の定期実行ジョブで自動更新しますので編集は不要です。\n",
        "\n",
        "## [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n",
        "\n",
        "- [[Owner記名ありページ]]\n",
        "\n",
        "## Ownerチームが不明だが必要なページ群\n",
        "\n",
        "- [[Ownerチームが不明だが必要なページ]]\n",
        "\n",
        "## Ownerチーム・要or不要が不明なページ群\n",
        "\n",
        "- [[Ownerチーム・要or不要が不明なページ]]\n",
        "\n",
        "## Owner記名なし\n",
        "\n",
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
        "## Wiki ページの運用ルール\n",
        "\n",
        "このページは Category ごとに Wiki をグルーピングして一覧化しています。\n",
        "\n",
        "Category が不明だと、保守性と検索性の悪化が発生します。  \n",
        "治安維持のため、各ページの冒頭に `Category: カテゴリー名` を明記して頂きますようよろしくお願いします。\n",
        "\n",
        "なお、Home・Sidebar は専用の定期実行ジョブで自動更新しますので編集は不要です。\n",
        "\n",
        "## test-category\n",
        "\n",
        "- [[Category記載ありページ]]\n",
        "\n",
        "## Category記載なし\n",
        "\n",
        "- [[Category記載なしページ1]]\n",
        "- [[Category記載なしページ2]]\n"
      ]
    end
  end
end

module English
  class OwnedHomeTest < HomeTest
    def setup
      super(template_lang: 'en')
    end

    def test_self_run
      assert_equal(home_passage.join, home)
    end

    private

    def home_passage
      [
        "## How to Manage Wiki Pages\n",
        "\n",
        "This Home page manage wikis by owner group.\n",
        "\n",
        "Absence of ownership declaration worsens maintainability and searchability because it makes ambiguous which team the responsibility belongs to.  \n",
        "Kindly make sure to articulate `Owner: @OWNER_TEAM` of the top of each of your wiki page to avoid it.\n",
        "\n",
        "Also, please keep in mind that you do not have to edit Home and Sidebar by yourself, which are automatically updated by a GitHub Actions cron job.\n",
        "\n",
        "## [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n",
        "\n",
        "- [[Owner記名ありページ]]\n",
        "\n",
        "## Ownerチームが不明だが必要なページ群\n",
        "\n",
        "- [[Ownerチームが不明だが必要なページ]]\n",
        "\n",
        "## Ownerチーム・要or不要が不明なページ群\n",
        "\n",
        "- [[Ownerチーム・要or不要が不明なページ]]\n",
        "\n",
        "## Owner記名なし\n",
        "\n",
        "- [[Owner記名なしページ1]]\n",
        "- [[Owner記名なしページ2]]\n"
      ]
    end
  end

  class PlainHomeTest < HomeTest
    def setup
      super(genre: '-c', template_lang: 'en')
    end

    def test_self_run
      assert_equal(home_passage.join, home)
    end

    private

    def home_passage
      [
        "## How to Manage Wiki Pages\n",
        "\n",
        "This Home page manage wikis by category group.\n",
        "\n",
        "Absence of category declaration worsens maintainability and searchability.  \n",
        "Kindly make sure to articulate `Category: CATEGORY_NAME` of the top of each of your wiki page to avoid it.\n",
        "\n",
        "Also, please keep in mind that you do not have to edit Home and Sidebar by yourself, which are automatically updated by a GitHub Actions cron job.\n",
        "\n",
        "## test-category\n",
        "\n",
        "- [[Category記載ありページ]]\n",
        "\n",
        "## Category記載なし\n",
        "\n",
        "- [[Category記載なしページ1]]\n",
        "- [[Category記載なしページ2]]\n"
      ]
    end
  end
end
