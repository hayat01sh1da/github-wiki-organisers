require_relative '../src/home'
require_relative '../src/sidebar'

genre, *_ = ARGV

puts '==================== Categorizing the Entire github-wiki-organisers Wiki Pages... ===================='

puts '========== Organising Home... =========='

home_url = case genre
when '-o', '--owner', '-c', '--category'
  Home.run(genre:)
else
  Home.run
end

puts "Check out An Up-to-date Wiki List on Home at #{home_url} !!"
puts "========== Done Organising Home 🎉 ==========\n\n"

puts '========== Organising Sidebar... =========='

home_url = case genre
when '-o', '--owner', '-c', '--category'
  Sidebar.run(genre:)
when
  Sidebar.run
end

puts "Check out An Up-to-date Wiki List on Sidebar at #{home_url} !!"
puts "========== Done Organising Home 🎉 =========="

puts '==================== Done Categorizing the Entire github-wiki-organisers Wiki Pages 🎉 ===================='
