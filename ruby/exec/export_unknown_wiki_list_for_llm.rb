require_relative '../src/unknown_wiki_list_exporter_for_llm'

group_by, language, *_ = ARGV
params = { group_by:, language: }.reject { |_, value| value.empty? }

puts '-------------------- Exporting Unknown Wiki List... --------------------'
path_to_export = UnknownWikiListExporterForLLM.run(**params)
puts "\n"
puts "Check it out result on '#{path_to_export}' !!"
puts "\n"
puts '-------------------- Done Exporting Unknown Wiki List 🎉 --------------------'
