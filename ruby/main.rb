require_relative './src/directory'
require_relative './src/home'
require_relative './src/sidebar'

puts '==================== Categorizing the Entire aya-issues Wiki Pages... ===================='

puts '========== Tidying Directories... =========='
mkdir_results, mv_wikis_to_dir_results, delete_empty_dir_results = Directory.run
puts '===== Making Directories by Owner Unit... ====='
mkdir_results.each { |mkdir_result| puts mkdir_result }
puts "===== Done Making Directories by Owner Unit 🎉 =====\n\n"
puts "===== Moving Files to Owner's Directories... ====="
mv_wikis_to_dir_results.each { |mv_wikis_to_dir_result| puts mv_wikis_to_dir_result }
puts "===== Done Moving Files to Owner's Directories 🎉 =====\n\n"
puts '===== Deleting Empty Directories... ====='
delete_empty_dir_results.each { |delete_empty_dir_result| puts delete_empty_dir_result }
puts '===== Done Deleting Empty Directories 🎉 ====='
puts "========== Done Tidying Directories 🎉 ==========\n\n"

puts '========== Tidying Home... =========='
home_url = Home.run
puts "Check out An Up-to-date Wiki List on Home at #{home_url} !!"
puts "========== Done Tidying Home 🎉 ==========\n\n"

puts '========== Tidying Sidebar... =========='
Sidebar.run
puts "Check out An Up-to-date Wiki List on Sidebar at #{home_url} !!"
puts "========== Done Tidying Home 🎉 =========="

puts '==================== Done Categorizing the Entire aya-issues Wiki Pages 🎉 ===================='
