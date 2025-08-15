require_relative '../src/home'
require_relative '../src/sidebar'

group_by, language, home_overflow, *_ = ARGV

puts '-------------------- Categorising the Entire github-wiki-organisers Wiki Pages... --------------------'
puts "\n"
puts '-------------------- Organising Home... --------------------'
home_url = case group_by
when 'Owner'
  if home_overflow
    Home.run(group_by:, home_overflow:)
  end
when 'Category'
  Home.run(group_by:)

  case language
  when 'English', 'Japanese'
    Home.run(group_by:, language:)
  end
else
  Home.run
end
puts "Check out an Up-to-date Wiki List on Home at '#{home_url}' !!"
puts '-------------------- Done Organising Home 🎉 --------------------'
puts "\n"
puts '-------------------- Organising Sidebar... --------------------'
case group_by
when 'Owner', 'Category'
  Sidebar.run(group_by:)

  case language
  when 'English', 'Japanese'
    Sidebar.run(group_by:, language:)
  end
else
  Sidebar.run
end
puts "Check out an Up-to-date Wiki List on Sidebar at '#{home_url}' !!"
puts '-------------------- Done Organising Sidebar 🎉 --------------------'
puts "\n"
puts '-------------------- Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 --------------------'
