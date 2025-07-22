require_relative './application_test'
require_relative '../src/sidebar'

class SidebarTest < ApplicationTest
  def setup(genre: '-o')
    super(genre:)
    Sidebar.run(base_path:, genre:)
    @path_to_sidebar = File.join(base_path, '_Sidebar.md')
    @sidebar         = File.read(path_to_sidebar)
  end

  private

  attr_reader :path_to_sidebar, :sidebar
end

class OwnedSidebarTest < SidebarTest
  def test_self_run
    assert_equal(sidebar, wiki_list.join)
  end

  private

  def wiki_list
    [
      "- [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n",
      "  - [[Owner記名ありページ]]\n",
      "- Ownerチームが不明だが必要なページ群\n",
      "  - [[Ownerチームが不明だが必要なページ]]\n",
      "- Ownerチーム・要or不要が不明なページ群\n",
      "  - [[Ownerチーム・要or不要が不明なページ]]\n",
      "- Owner記名なし\n",
      "  - [[Owner記名なしページ1]]\n",
      "  - [[Owner記名なしページ2]]\n"
    ]
  end
end

class PlainSidebarTest < SidebarTest
  def setup
    super(genre: '-c')
  end

  def test_self_run
    assert_equal(sidebar, wiki_list.join)
  end

  private

  def wiki_list
    [
      "- test-category\n",
      "  - [[Category記載ありページ]]\n",
      "- Category記載なし\n",
      "  - [[Category記載なしページ1]]\n",
      "  - [[Category記載なしページ2]]\n"
    ]
  end
end
