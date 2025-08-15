require_relative './application_test'
require_relative '../src/sidebar'

class SidebarTest < ApplicationTest
  def setup(group_by: 'Owner', language: 'English')
    super(group_by:, language:)
    Sidebar.run(base_path:, group_by:, language:)
    @path_to_sidebar = File.join(base_path, '_Sidebar.md')
    @sidebar         = File.read(path_to_sidebar)
  end

  private

  attr_reader :path_to_sidebar, :sidebar

  module English
    class OwnedSidebarTest < SidebarTest
      def test_self_run
        assert_equal(wiki_list.join, sidebar)
      end

      private

      def wiki_list
        [
          "- [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n",
          "  - [[Owned Wiki]]\n",
          "- Unknown Owner nor Necessity\n",
          "  - [[Unknown Owner nor Necessity Wiki]]\n",
          "- Unowned but Necessary\n",
          "  - [[Unowned but Necessary Wiki]]\n",
          "- Unowned\n",
          "  - [[Unowned Wiki 1]]\n",
          "  - [[Unowned Wiki 2]]\n"
        ]
      end
    end

    class PlainSidebarTest < SidebarTest
      def setup
        super(group_by: 'Category')
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
          "  - [[Uncategorised Wiki 1]]\n",
          "  - [[Uncategorised Wiki 2]]\n"
        ]
      end
    end
  end

  module Japanese
    class OwnedSidebarTest < SidebarTest
      def setup
        super(language: 'Japanese')
      end

      def test_self_run
        assert_equal(wiki_list.join, sidebar)
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
        super(group_by: 'Category', language: 'Japanese')
      end

      def test_self_run
        assert_equal(wiki_list.join, sidebar)
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
  end
end
