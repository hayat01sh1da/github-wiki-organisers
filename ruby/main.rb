require_relative './src/directory'
require_relative './src/home'
require_relative './src/sidebar'

puts '==================== Categosizing the Entire aya-issues Wiki pages... ===================='
Directory.run
Home.run
Sidebar.run
puts '==================== Done categorising the Entire aya-issues Wiki pages 🎉 ===================='
