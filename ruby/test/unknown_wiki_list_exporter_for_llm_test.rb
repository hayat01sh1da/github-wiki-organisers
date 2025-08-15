require_relative './application_test'
require_relative '../src/unknown_wiki_list_exporter_for_llm'

class UnknownWikiListExporterForLLMTest < ApplicationTest
  def setup(group_by: '-o', language: '-en')
    super(group_by:, language:)
    UnknownWikiListExporterForLLM.run(base_path:, group_by:, language:)
    @path_to_unknown_wiki_list_for_llm = File.join(base_path, 'unknown_wiki_list_for_llm.txt')
    @unknown_wiki_list_for_llm         = File.read(path_to_unknown_wiki_list_for_llm)
  end

  private

  attr_reader :path_to_unknown_wiki_list_for_llm, :unknown_wiki_list_for_llm

  module English
    class OwnershipTest < UnknownWikiListExporterForLLMTest
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

    class CategoryTest < UnknownWikiListExporterForLLMTest
      def setup
        super(group_by: '-c')
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
    class OwnershipTest < UnknownWikiListExporterForLLMTest
      def setup
        super(language: '-ja')
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

    class CategoryTest < UnknownWikiListExporterForLLMTest
      def setup
        super(group_by: '-c', language: '-ja')
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
end
