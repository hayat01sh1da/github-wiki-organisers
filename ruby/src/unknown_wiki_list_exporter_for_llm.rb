require_relative './application'

class UnknownWikiListExporterForLLM < Application
  def initialize(base_path:, group_by:, language:)
    super(base_path:, group_by:, language:)
    @path_to_export = File.join(base_path, 'unknown_wiki_list_for_llm.txt')
  end

  def run
    File.open(path_to_export, 'wb') { |f| f.puts(unknown_wiki_list_for_llm) }
    path_to_export
  end

  private

  attr_reader :path_to_export

  # @return [Array<String>]
  def target_namespace
    case group_by
    when 'Owner'
      case language
      when 'English'
        'Unknown Owner nor Necessity'
      when 'Japanese'
        'Ownerチーム・要or不要が不明なページ群'
      end
    when 'Category'
      case language
      when 'English'
        'Uncategorised'
      when 'Japanese'
        'Category記載なし'
      end
    end
  end

  # @return [Array<String>]
  def unknown_wiki_list_for_llm
    @unknown_wiki_list_for_llm ||= plain_wiki_maps.select { |namespace, _|
      target_namespace.include?(namespace)
    }.then {
      it.values.flatten
    }
  end
end
