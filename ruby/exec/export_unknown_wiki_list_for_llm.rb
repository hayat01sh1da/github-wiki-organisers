require_relative '../src/unknown_wiki_list_exporter_for_llm'

group_by, language, *_ = ARGV

puts '-------------------- Exporting Unknown Wiki List... --------------------'
path_to_export = case group_by
when 'Owner', 'Category'
  UnknownWikiListExporterForLLM.run(group_by:)

  case language
  when 'English', 'Japanese'
    UnknownWikiListExporterForLLM.run(group_by:, language:)
  end
else
  UnknownWikiListExporterForLLM.run
end
puts "\n"
puts "Check it out result on '#{path_to_export}' !!"
puts "\n"
puts '-------------------- Done Exporting Unknown Wiki List 🎉 --------------------'
