require_relative '../src/unowned_wiki_list_exporter'

puts '==================== Exporting Unowned Wiki List... ===================='
count_list_by_namespace, path_to_export = UnknownWikiListExporter.run
puts "Here is the result:\n\n"

count_list_by_namespace.each { |count_list|
  puts count_list
}

puts "\nCheck it out result on '#{path_to_export}' !!"
puts '==================== Done Exporting Unowned Wiki List 🎉 ===================='
