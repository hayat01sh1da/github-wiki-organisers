require_relative './src/directory'
require_relative './src/home'
require_relative './src/sidebar'

puts '==================== Categorizing the Entire aya-issues Wiki Pages... ===================='

puts '========== Tidying Home... =========='
home_url = Home.run
puts "Check out An Up-to-date Wiki List on Home at #{home_url} !!"
puts "========== Done Tidying Home 🎉 ==========\n\n"

puts '========== Tidying Sidebar... =========='
Sidebar.run
puts "Check out An Up-to-date Wiki List on Sidebar at #{home_url} !!"
puts "========== Done Tidying Home 🎉 =========="

puts '==================== Done Categorizing the Entire aya-issues Wiki Pages 🎉 ===================='
