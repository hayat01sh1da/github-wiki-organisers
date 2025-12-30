require_relative '../src/home'
require_relative '../src/sidebar'

group_by, language, home_overflow, *_ = ARGV
params = { group_by:, language:, home_overflow: }.reject { |_, value| value.empty? }

puts '-------------------- Categorising the Entire github-wiki-organisers Wiki Pages... --------------------'
puts "\n"
puts '-------------------- Organising Home... --------------------'
home_url = Home.run(**params)
puts "Check out an Up-to-date Wiki List on Home at '#{home_url}' !!"
puts '-------------------- Done Organising Home 🎉 --------------------'
puts "\n"
puts '-------------------- Organising Sidebar... --------------------'
Sidebar.run(**params)
puts "Check out an Up-to-date Wiki List on Sidebar at '#{home_url}' !!"
puts '-------------------- Done Organising Sidebar 🎉 --------------------'
puts "\n"
puts '-------------------- Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 --------------------'
