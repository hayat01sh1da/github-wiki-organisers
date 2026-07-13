# frozen_string_literal: true

require_relative 'lib/github_wiki_organiser/version'

Gem::Specification.new do |spec|
  spec.name    = 'github_wiki_organiser'
  spec.version = GithubWikiOrganiser::VERSION
  spec.authors = ['hayat01sh1da']

  spec.summary     = 'Organise GitHub wiki Home and _Sidebar pages by owner or category.'
  spec.description = 'Generates Home.md and _Sidebar.md for a GitHub wiki by grouping pages by the ' \
                     'Owner/Category declared on the first line of each page (English and Japanese ' \
                     'labels built in, extensible via .wiki-organiser.yml), and exports reports of ' \
                     'the pages whose owner or category is unknown.'
  spec.homepage = 'https://github.com/hayat01sh1da/github-wiki-organisers'
  spec.license  = 'MIT'
  spec.required_ruby_version = '>= 3.4'

  spec.metadata['homepage_uri']          = spec.homepage
  spec.metadata['source_code_uri']       = spec.homepage
  spec.metadata['changelog_uri']         = "#{spec.homepage}/blob/master/CHANGELOG.md"
  spec.metadata['bug_tracker_uri']       = "#{spec.homepage}/issues"
  spec.metadata['rubygems_mfa_required'] = 'true'

  spec.files         = Dir['exe/*', 'lib/**/*.rb', 'lib/github_wiki_organiser/templates/**/*.md', 'sig/**/*.rbs',
                           'README.md', 'LICENSE.txt']
  spec.bindir        = 'exe'
  spec.executables   = ['wiki-organise']
  spec.require_paths = ['lib']
end
