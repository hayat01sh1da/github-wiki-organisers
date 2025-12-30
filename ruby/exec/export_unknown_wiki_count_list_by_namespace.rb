require_relative '../src/unknown_wiki_count_list_exporter'

group_by, language, *_ = ARGV
params = { group_by:, language: }.reject { |_, value| value.empty? }

puts '-------------------- Exporting Unknown Wiki Count List... --------------------'
count_list_by_namespace, path_to_export = UnknownWikiCountListExporter.run(**params)
puts "\n"
puts 'Here is the result:'
puts "\n"
puts '---------------------------------------'
count_list_by_namespace.each { |count_list|
  puts count_list
}
puts '---------------------------------------'
puts "\n"
puts "Check it out result on '#{path_to_export}' !!"
puts "\n"
puts '-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------'
