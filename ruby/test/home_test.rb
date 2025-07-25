require_relative './application_test'
require_relative '../src/home'

class HomeTest < ApplicationTest
  def setup(genre: '-o', template_lang: 'en')
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

module English
  class OwnedHomeTest < HomeTest
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
        "- [[Owned Wiki]]\n",
        "\n",
        "## Unknown Owner nor Necessity\n",
        "\n",
        "- [[Unknown Owner nor Necessity Wiki]]\n",
        "\n",
        "## Unowned but Necessary\n",
        "\n",
        "- [[Unowned but Necessary Wiki]]\n",
        "\n",
        "## Unowned\n",
        "\n",
        "- [[Unowned Wiki 1]]\n",
        "- [[Unowned Wiki 2]]\n"
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
        "- [[Categorised Wiki]]\n",
        "\n",
        "## Uncategorised\n",
        "\n",
        "- [[Uncategorised Wiki1]]\n",
        "- [[Uncategorised Wiki2]]\n"
      ]
    end
  end
end

module Japanese
  class OwnedHomeTest < HomeTest
    def setup
      super(genre: '-o', template_lang: 'ja')
    end

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
        "- [[Owned Wiki]]\n",
        "\n",
        "## Unknown Owner nor Necessity\n",
        "\n",
        "- [[Unknown Owner nor Necessity Wiki]]\n",
        "\n",
        "## Unowned but Necessary\n",
        "\n",
        "- [[Unowned but Necessary Wiki]]\n",
        "\n",
        "## Unowned\n",
        "\n",
        "- [[Unowned Wiki 1]]\n",
        "- [[Unowned Wiki 2]]\n"
      ]
    end
  end

  class PlainHomeTest < HomeTest
    def setup
      super(genre: '-c', template_lang: 'ja')
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
        "- [[Categorised Wiki]]\n",
        "\n",
        "## Uncategorised\n",
        "\n",
        "- [[Uncategorised Wiki1]]\n",
        "- [[Uncategorised Wiki2]]\n"
      ]
    end
  end
end
