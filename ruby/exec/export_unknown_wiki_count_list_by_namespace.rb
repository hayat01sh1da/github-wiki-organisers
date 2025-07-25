require_relative '../src/unknown_wiki_count_list_exporter'

genre, language, *_ = ARGV

puts '-------------------- Exporting Unknown Wiki Count List... --------------------'
count_list_by_namespace, path_to_export = case genre
when '-o', '--owner', '-c', '--category'
  case language
  when '-en', '-ja'
    UnknownWikiCountListExporter.run(genre:, language:)
  end
else
  UnknownWikiCountListExporter.run
end
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
