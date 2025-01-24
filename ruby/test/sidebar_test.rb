require_relative './application_test'
require_relative '../src/sidebar'

class SidebarTest < ApplicationTest
  def setup
    super
    Sidebar.run(base_path:)
    path_to_sidebar = File.join(base_path, '_Sidebar.md')
    @sidebar        = IO.read(path_to_sidebar)
  end

  def test_self_run
    assert_equal(sidebar, wiki_list.join)
  end

  private

  attr_reader :sidebar

  def wiki_list
    list  = []
    list << "- [@test-owner](https://github.com/orgs/quipper/teams/test-owner)\n"
    list << "  - [[Owner記名ありページ]]\n"
    list << "- Ownerチームが不明だが必要なページ群\n"
    list << "  - [[Ownerチームが不明だが必要なページ]]\n"
    list << "- Ownerチーム・要or不要が不明なページ群\n"
    list << "  - [[Ownerチーム・要or不要が不明なページ]]\n"
    list << "- Owner記名なし\n"
    list << "  - [[Owner記名なしページ1]]\n"
    list << "  - [[Owner記名なしページ2]]\n"
  end
end
