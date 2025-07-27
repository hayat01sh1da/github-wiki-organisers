require_relative './application'

class UnknownWikiListExporterForLLM < Application
  def initialize(base_path:, genre:, language:)
    super(base_path:, genre:, language:)
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
    case genre
    when '-o', '--owner'
      case language
      when '-en'
        'Unknown Owner nor Necessity'
      when '-ja'
        'Ownerチーム・要or不要が不明なページ群'
      end
    when '-c', '--category'
      case language
      when '-en'
        'Uncategorised'
      when '-ja'
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
