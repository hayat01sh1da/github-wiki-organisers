require_relative '../src/unknown_wiki_list_exporter_for_llm'

genre, language, *_ = ARGV

puts '-------------------- Exporting Unknown Wiki List... --------------------'
path_to_export = case genre
when '-o', '--owner', '-c', '--category'
  UnknownWikiListExporterForLLM.run(genre:)

  case language
  when '-en', '-ja'
    UnknownWikiListExporterForLLM.run(genre:, language:)
  end
else
  UnknownWikiListExporterForLLM.run
end
puts "\n"
puts "Check it out result on '#{path_to_export}' !!"
puts "\n"
puts '-------------------- Done Exporting Unknown Wiki List 🎉 --------------------'
