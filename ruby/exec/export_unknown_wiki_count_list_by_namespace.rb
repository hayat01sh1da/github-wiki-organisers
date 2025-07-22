require_relative '../src/unknown_wiki_count_list_exporter'

genre, *_ = ARGV

puts '==================== Exporting Unowned Wiki List... ===================='
count_list_by_namespace, path_to_export = UnknownWikiCountListExporter.run(genre:)
puts "Here is the result:\n\n"

count_list_by_namespace.each { |count_list|
  puts count_list
}

puts "\nCheck it out result on '#{path_to_export}' !!"
puts '==================== Done Exporting Unowned Wiki List 🎉 ===================='
