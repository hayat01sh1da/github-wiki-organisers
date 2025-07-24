require_relative '../src/home'
require_relative '../src/sidebar'

genre, *_ = ARGV

puts '==================== Categorising the Entire github-wiki-organisers Wiki Pages... ===================='

puts '========== Organising Home... =========='

home_url = case genre
when '-o', '--owner', '-c', '--category'
  Home.run(genre:)
else
  Home.run
end

puts "Check out an Up-to-date Wiki List on Home at #{home_url} !!"
puts "========== Done Organising Home 🎉 ==========\n\n"

puts '========== Organising Sidebar... =========='

case genre
when '-o', '--owner', '-c', '--category'
  Sidebar.run(genre:)
when
  Sidebar.run
end

puts "Check out an Up-to-date Wiki List on Sidebar at #{home_url} !!"
puts "========== Done Organising Home 🎉 =========="

puts '==================== Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 ===================='
