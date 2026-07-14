# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'spreen_wiki/version'
require_relative 'spreen_wiki/configuration'
require_relative 'spreen_wiki/application'
require_relative 'spreen_wiki/home'
require_relative 'spreen_wiki/sidebar'
require_relative 'spreen_wiki/unknown_wiki_count_list_exporter'
require_relative 'spreen_wiki/unknown_wiki_list_exporter_for_llm'
require_relative 'spreen_wiki/cli'

# Spreens a GitHub wiki — the falcon's stoop, then the preen: generates
# Home.md and _Sidebar.md grouped by the Owner/Category declared on the
# first line of each page, and exports reports of the pages whose owner
# or category is unknown.
module SpreenWiki
end
