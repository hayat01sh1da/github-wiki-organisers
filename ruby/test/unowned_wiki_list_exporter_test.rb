require_relative './application_test'
require_relative '../src/unowned_wiki_list_exporter'

class UnknownWikiListExporterTest < ApplicationTest
  def setup
    super
    UnknownWikiListExporter.run(base_path:)
    path_to_unowned_wiki_count_list = File.join(base_path, 'unowned_wiki_count_list_by_namespace.txt')
    @unowned_wiki_count_list        = IO.read(path_to_unowned_wiki_count_list)
  end

  private

  attr_reader :unowned_wiki_count_list
end

class RegularCase < UnknownWikiListExporterTest
  def test_self_run
    assert_equal(unowned_wiki_count_list, unowned_wiki_count_list_by_namespace.join)
  end

  private

  def unowned_wiki_count_list_by_namespace
    list  = []
    list << "Ownerチームが不明だが必要なページ群: 1件\n"
    list << "Ownerチーム・要or不要が不明なページ群: 1件\n"
    list << "Owner記名なし: 2件\n"
  end
end

class IrregularCase < UnknownWikiListExporterTest
  def test_self_run
    assert_equal(unowned_wiki_count_list, unowned_wiki_count_list_by_namespace.join)
  end

  private

  def unowned_wiki_count_list_by_namespace
    list  = []
    list << "Ownerチームが不明だが必要なページ群: 1件\n"
    list << "Ownerチーム・要or不要が不明なページ群: 1件\n"
    list << "Owner記名なし: 0件\n"
  end

  def test_file_maps
    {
      'Owner記名ありページ.md' => 'Owner: @test-owner',
      'Ownerチームが不明だが必要なページ.md' => 'Owner: Ownerチームが不明だが必要なページ群',
      'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群'
    }
  end
end
