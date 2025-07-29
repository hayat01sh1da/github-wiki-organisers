require_relative '../src/home'
require_relative '../src/sidebar'

genre, language, *_ = ARGV

puts '-------------------- Categorising the Entire github-wiki-organisers Wiki Pages... --------------------'
puts "\n"
puts '-------------------- Organising Home... --------------------'
home_url = case genre
when '-o', '--owner', '-c', '--category'
  Home.run(genre:)

  case language
  when '-en', '-ja'
    Home.run(genre:, language:)
  end
else
  Home.run
end
puts "Check out an Up-to-date Wiki List on Home at '#{home_url}' !!"
puts '-------------------- Done Organising Home 🎉 --------------------'
puts "\n"
puts '-------------------- Organising Sidebar... --------------------'
case genre
when '-o', '--owner', '-c', '--category'
  Sidebar.run(genre:)

  case language
  when '-en', '-ja'
    Sidebar.run(genre:, language:)
  end
else
  Sidebar.run
end
puts "Check out an Up-to-date Wiki List on Sidebar at '#{home_url}' !!"
puts '-------------------- Done Organising Sidebar 🎉 --------------------'
puts "\n"
puts '-------------------- Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 --------------------'
