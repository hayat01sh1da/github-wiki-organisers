# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'github_wiki_organiser/version'
require_relative 'github_wiki_organiser/configuration'
require_relative 'github_wiki_organiser/application'
require_relative 'github_wiki_organiser/home'
require_relative 'github_wiki_organiser/sidebar'
require_relative 'github_wiki_organiser/unknown_wiki_count_list_exporter'
require_relative 'github_wiki_organiser/unknown_wiki_list_exporter_for_llm'
require_relative 'github_wiki_organiser/cli'

# Organises a GitHub wiki: generates Home.md and _Sidebar.md grouped by the
# Owner/Category declared on the first line of each page, and exports reports
# of the pages whose owner or category is unknown.
module GithubWikiOrganiser
end
