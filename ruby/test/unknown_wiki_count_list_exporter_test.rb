require_relative './application_test'
require_relative '../src/unknown_wiki_count_list_exporter'

class UnknownWikiCountListExporterTest < ApplicationTest
  def setup(genre: '-o')
    super(genre:)
    UnknownWikiCountListExporter.run(base_path:, genre:)
    @path_to_unknown_wiki_count_list = File.join(base_path, 'unknown_wiki_count_list_by_namespace.txt')
    @unknown_wiki_count_list         = IO.read(path_to_unknown_wiki_count_list)
  end

  private

  attr_reader :path_to_unknown_wiki_count_list, :unknown_wiki_count_list
end

class OwnershipTest < UnknownWikiCountListExporterTest
  class RegularCase1 < OwnershipTest
    def test_self_run
      assert_equal(unknown_wiki_count_list, unknown_wiki_count_list_by_namespace.join)
    end

    private

    def unknown_wiki_count_list_by_namespace
      [
        "Ownerチームが不明だが必要なページ群: 1件\n",
        "Ownerチーム・要or不要が不明なページ群: 1件\n",
        "Owner記名なし: 2件\n"
      ]
    end
  end

  class RegularCase2 < OwnershipTest
    def test_self_run
      assert_equal(unknown_wiki_count_list, unknown_wiki_count_list_by_namespace.join)
    end

    private

    def unknown_wiki_count_list_by_namespace
      [
        "Ownerチームが不明だが必要なページ群: 1件\n",
        "Ownerチーム・要or不要が不明なページ群: 1件\n",
        "Owner記名なし: 2件\n"
      ]
    end

    def test_file_maps
      {
        'Ownerチームが不明だが必要なページ.md' => 'Owner: Ownerチームが不明だが必要なページ群',
        'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群',
        'Owner記名なしページ1.md' => '',
        'Owner記名なしページ2.md' => 'This is a sample Wiki'
      }
    end
  end

  class IrregularCase1 < OwnershipTest
    def test_self_run
      assert_equal(unknown_wiki_count_list, unknown_wiki_count_list_by_namespace.join)
    end

    private

    def unknown_wiki_count_list_by_namespace
      [
        "Ownerチームが不明だが必要なページ群: 0件\n",
        "Ownerチーム・要or不要が不明なページ群: 1件\n",
        "Owner記名なし: 2件\n"
      ]
    end

    def test_file_maps
      {
        'Owner記名ありページ.md' => 'Owner: @test-owner',
        'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群',
        'Owner記名なしページ1.md' => '',
        'Owner記名なしページ2.md' => 'This is a sample Wiki'
      }
    end
  end

  class IrregularCase2 < OwnershipTest
    def test_self_run
      assert_equal(unknown_wiki_count_list, unknown_wiki_count_list_by_namespace.join)
    end

    private

    def unknown_wiki_count_list_by_namespace
      [
        "Ownerチームが不明だが必要なページ群: 1件\n",
        "Ownerチーム・要or不要が不明なページ群: 0件\n",
        "Owner記名なし: 2件\n"
      ]
    end

    def test_file_maps
      {
        'Owner記名ありページ.md' => 'Owner: @test-owner',
        'Ownerチームが不明だが必要なページ.md' => 'Owner: Ownerチームが不明だが必要なページ群',
        'Owner記名なしページ1.md' => '',
        'Owner記名なしページ2.md' => 'This is a sample Wiki'
      }
    end
  end

  class IrregularCase3 < OwnershipTest
    def test_self_run
      assert_equal(unknown_wiki_count_list, unknown_wiki_count_list_by_namespace.join)
    end

    private

    def unknown_wiki_count_list_by_namespace
      [
        "Ownerチームが不明だが必要なページ群: 1件\n",
        "Ownerチーム・要or不要が不明なページ群: 1件\n",
        "Owner記名なし: 0件\n"
      ]
    end

    def test_file_maps
      {
        'Owner記名ありページ.md' => 'Owner: @test-owner',
        'Ownerチームが不明だが必要なページ.md' => 'Owner: Ownerチームが不明だが必要なページ群',
        'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群'
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
      assert_equal(unknown_wiki_count_list, unknown_wiki_count_list_by_namespace.join)
    end

    private

    def unknown_wiki_count_list_by_namespace
      [
        "Category記載なし: 2件\n"
      ]
    end
  end

  class IrregularCase < CategoryTest
    def test_self_run
      assert_equal(unknown_wiki_count_list, unknown_wiki_count_list_by_namespace.join)
    end

    private

    def unknown_wiki_count_list_by_namespace
      [
        "Category記載なし: 4件\n"
      ]
    end

    def test_file_maps
      {
        'Owner記名ありページ.md' => 'Owner: @test-owner',
        'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群',
        'Owner記名なしページ1.md' => '',
        'Owner記名なしページ2.md' => 'This is a sample Wiki'
      }
    end
  end
end
