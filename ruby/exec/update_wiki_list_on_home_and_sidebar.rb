require_relative '../src/home'
require_relative '../src/sidebar'

puts '==================== Categorizing the Entire github-wiki-organisers Wiki Pages... ===================='

puts '========== Organising Home... =========='
home_url = Home.run
puts "Check out An Up-to-date Wiki List on Home at #{home_url} !!"
puts "========== Done Organising Home 🎉 ==========\n\n"

puts '========== Organising Sidebar... =========='
Sidebar.run
puts "Check out An Up-to-date Wiki List on Sidebar at #{home_url} !!"
puts "========== Done Organising Home 🎉 =========="

puts '==================== Done Categorizing the Entire github-wiki-organisers Wiki Pages 🎉 ===================='
