require_relative './application_test'
require_relative '../src/unknown_wiki_list_exporter_for_llm'

class UnknownWikiListExporterForLLMTest < ApplicationTest
  def setup(genre: '-o', language: '-en')
    super(genre:, language:)
    UnknownWikiListExporterForLLM.run(base_path:, genre:, language:)
    @path_to_unknown_wiki_list_for_llm = File.join(base_path, 'unknown_wiki_list_for_llm.txt')
    @unknown_wiki_list_for_llm         = IO.read(path_to_unknown_wiki_list_for_llm)
  end

  private

  attr_reader :path_to_unknown_wiki_list_for_llm, :unknown_wiki_list_for_llm
end

module English
  class UnknownWikiListExporterForLLMTest::OwnershipTest < UnknownWikiListExporterForLLMTest
    def test_self_run
      assert_equal(unknown_wiki_list.join("\n"), unknown_wiki_list_for_llm.chomp)
    end

    private

    def unknown_wiki_list
      [
        'Unknown Owner nor Necessity Wiki.md'
      ]
    end
  end

  class UnknownWikiListExporterForLLMTest::CategoryTest < UnknownWikiListExporterForLLMTest
    def setup
      super(genre: '-c')
    end

    def test_self_run
      assert_equal(unknown_wiki_list.join("\n"), unknown_wiki_list_for_llm.chomp)
    end

    private

    def unknown_wiki_list
      [
        'Uncategorised Wiki 1.md',
        'Uncategorised Wiki 2.md'
      ]
    end
  end
end

module Japanese
  class UnknownWikiListExporterForLLMTest::OwnershipTest < UnknownWikiListExporterForLLMTest
    def setup
      super(genre: '-o', language: '-ja')
    end

    def test_self_run
      assert_equal(unknown_wiki_list.join("\n"), unknown_wiki_list_for_llm.chomp)
    end

    private

    def unknown_wiki_list
      [
        'Ownerチーム・要or不要が不明なページ.md'
      ]
    end
  end

  class UnknownWikiListExporterForLLMTest::CategoryTest < UnknownWikiListExporterForLLMTest
    def setup
      super(genre: '-c', language: '-ja')
    end

    def test_self_run
      assert_equal(unknown_wiki_list.join("\n"), unknown_wiki_list_for_llm.chomp)
    end

    private

    def unknown_wiki_list
      [
        'Category記載なしページ1.md',
        'Category記載なしページ2.md'
      ]
    end
  end
end
