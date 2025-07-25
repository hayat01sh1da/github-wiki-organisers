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
    assert_equal(wiki_list.join, sidebar)
  end

  private

  def wiki_list
    [
      "- [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n",
      "  - [[Owned Wiki]]\n",
      "- Unowned but Necessary\n",
      "  - [[Unowned but Necessary Wiki]]\n",
      "- Unknown Owner nor Necessity\n",
      "  - [[Unknown Owner nor Necessity Wiki]]\n",
      "- Unowned\n",
      "  - [[Unowned Wiki 1]]\n",
      "  - [[Unowned Wiki 2]]\n"
    ]
  end
end

class PlainSidebarTest < SidebarTest
  def setup
    super(genre: '-c')
  end

  def test_self_run
    assert_equal(wiki_list.join, sidebar)
  end

  private

  def wiki_list
    [
      "- test-category\n",
      "  - [[Categorised Wiki]]\n",
      "- Uncategorised\n",
      "  - [[Uncategorised Wiki1]]\n",
      "  - [[Uncategorised Wiki2]]\n"
    ]
  end
end
