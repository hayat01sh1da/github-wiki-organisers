require_relative './application_test'
require_relative '../src/unknown_wiki_count_list_exporter'

class UnknownWikiCountListExporterTest < ApplicationTest
  def setup(genre: '-o', language: '-en')
    super(genre:, language:)
    UnknownWikiCountListExporter.run(base_path:, genre:, language:)
    @path_to_unknown_wiki_count_list = File.join(base_path, 'unknown_wiki_count_list_by_namespace.txt')
    @unknown_wiki_count_list         = File.read(path_to_unknown_wiki_count_list)
  end

  private

  attr_reader :path_to_unknown_wiki_count_list, :unknown_wiki_count_list
end

module English
  class OwnershipTest < UnknownWikiCountListExporterTest
    class RegularCase1 < OwnershipTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Unknown Owner nor Necessity: 1\n",
          "Unowned but Necessary: 1\n",
          "Unowned: 2\n"
        ]
      end
    end

    class RegularCase2 < OwnershipTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Unknown Owner nor Necessity: 1\n",
          "Unowned but Necessary: 1\n",
          "Unowned: 2\n"
        ]
      end

      def test_file_maps
        {
          'Unowned but Necessary Wiki.md' => 'Owner: Unowned but Necessary',
          'Unknown Owner nor Necessity Wiki.md' => 'Owner: Unknown Owner nor Necessity',
          'Unowned Wiki 1.md' => '',
          'Unowned Wiki 2.md' => 'This is a sample Wiki'
        }
      end
    end

    class IrregularCase1 < OwnershipTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Unknown Owner nor Necessity: 0\n",
          "Unowned but Necessary: 1\n",
          "Unowned: 2\n"
        ]
      end

      def test_file_maps
        {
          'Owned Wiki.md' => 'Owner: @test-owner',
          'Unowned but Necessary Wiki.md' => 'Owner: Unowned but Necessary',
          'Unowned Wiki 1.md' => '',
          'Unowned Wiki 2.md' => 'This is a sample Wiki'
        }
      end
    end

    class IrregularCase2 < OwnershipTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Unknown Owner nor Necessity: 1\n",
          "Unowned but Necessary: 0\n",
          "Unowned: 2\n"
        ]
      end

      def test_file_maps
        {
          'Owned Wiki.md' => 'Owner: @test-owner',
          'Unknown Owner nor Necessity Wiki.md' => 'Owner: Unknown Owner nor Necessity',
          'Unowned Wiki 1.md' => '',
          'Unowned Wiki 2.md' => 'This is a sample Wiki'
        }
      end
    end

    class IrregularCase3 < OwnershipTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Unknown Owner nor Necessity: 1\n",
          "Unowned but Necessary: 1\n",
          "Unowned: 0\n"
        ]
      end

      def test_file_maps
        {
          'Owned Wiki.md' => 'Owner: @test-owner',
          'Unowned but Necessary Wiki.md' => 'Owner: Unowned but Necessary',
          'Unknown Owner nor Necessity Wiki.md' => 'Owner: Unknown Owner nor Necessity'
        }
      end
    end
  end

  class CategoryTest < UnknownWikiCountListExporterTest
    def setup
      super(genre: '-c')
    end

    class RegularCase < CategoryTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Uncategorised: 2\n"
        ]
      end
    end

    class IrregularCase < CategoryTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Uncategorised: 5\n"
        ]
      end

      def test_file_maps
        {
          'Owned Wiki.md' => 'Owner: @test-owner',
          'Unowned but Necessary Wiki.md' => 'Owner: Unowned but Necessary',
          'Unknown Owner nor Necessity Wiki.md' => 'Owner: Unknown Owner nor Necessity',
          'Unowned Wiki 1.md' => '',
          'Unowned Wiki 2.md' => 'This is a sample Wiki'
        }
      end
    end
  end
end

module Japanese
  class OwnershipTest < UnknownWikiCountListExporterTest
    def setup
      super(language: '-ja')
    end

    class RegularCase1 < OwnershipTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Ownerチームが不明だが必要なページ群: 1\n",
          "Ownerチーム・要or不要が不明なページ群: 1\n",
          "Owner記名なし: 2\n"
        ]
      end
    end

    class RegularCase2 < OwnershipTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Ownerチームが不明だが必要なページ群: 1\n",
          "Ownerチーム・要or不要が不明なページ群: 1\n",
          "Owner記名なし: 2\n"
        ]
      end

      def test_file_maps
        {
          'Ownerチームが不明だが必要なページ.md' => 'Owner: Ownerチームが不明だが必要なページ群',
          'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群',
          'Owner記名なしページ1.md' => '',
          'Owner記名なしページ2.md' => 'サンプル Wiki'
        }
      end
    end

    class IrregularCase1 < OwnershipTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Ownerチームが不明だが必要なページ群: 1\n",
          "Ownerチーム・要or不要が不明なページ群: 0\n",
          "Owner記名なし: 2\n"
        ]
      end

      def test_file_maps
        {
          'Owner記名ありページ.md' => 'Owner: @test-owner',
          'Ownerチームが不明だが必要なページ.md' => 'Owner: Ownerチームが不明だが必要なページ群',
          'Owner記名なしページ1.md' => '',
          'Owner記名なしページ2.md' => 'サンプル Wiki'
        }
      end
    end

    class IrregularCase2 < OwnershipTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Ownerチームが不明だが必要なページ群: 0\n",
          "Ownerチーム・要or不要が不明なページ群: 1\n",
          "Owner記名なし: 2\n"
        ]
      end

      def test_file_maps
        {
          'Owner記名ありページ.md' => 'Owner: @test-owner',
          'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群',
          'Owner記名なしページ1.md' => '',
          'Owner記名なしページ2.md' => 'サンプル Wiki'
        }
      end
    end

    class IrregularCase3 < OwnershipTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Ownerチームが不明だが必要なページ群: 1\n",
          "Ownerチーム・要or不要が不明なページ群: 1\n",
          "Owner記名なし: 0\n"
        ]
      end

      def test_file_maps
        {
          'Owner記名ありページ.md' => 'Owner: @test-owner',
          'Ownerチームが不明だが必要なページ.md' => 'Owner: Ownerチームが不明だが必要なページ群',
          'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群',
        }
      end
    end
  end

  class CategoryTest < UnknownWikiCountListExporterTest
    def setup
      super(genre: '-c', language: '-ja')
    end

    class RegularCase < CategoryTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Category記載なし: 2\n"
        ]
      end
    end

    class IrregularCase < CategoryTest
      def test_self_run
        assert_equal(unknown_wiki_count_list_by_namespace.join, unknown_wiki_count_list)
      end

      private

      def unknown_wiki_count_list_by_namespace
        [
          "Category記載なし: 5\n"
        ]
      end

      def test_file_maps
        {
          'Owner記名ありページ.md' => 'Owner: @test-owner',
          'Ownerチームが不明だが必要なページ.md' => 'Owner: Ownerチームが不明だが必要なページ群',
          'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群',
          'Owner記名なしページ1.md' => '',
          'Owner記名なしページ2.md' => 'サンプル Wiki'
        }
      end
    end
  end
end
