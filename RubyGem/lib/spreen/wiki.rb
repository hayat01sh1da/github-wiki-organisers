# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'wiki/version'
require_relative 'wiki/configuration'
require_relative 'wiki/application'
require_relative 'wiki/home'
require_relative 'wiki/sidebar'
require_relative 'wiki/unknown_wiki_count_list_exporter'
require_relative 'wiki/unknown_wiki_list_exporter_for_llm'
require_relative 'wiki/cli'

module Spreen
  # Spreens a GitHub wiki — the falcon's stoop, then the preen: generates
  # Home.md and _Sidebar.md grouped by the Owner/Category declared on the
  # first line of each page, and exports reports of the pages whose owner
  # or category is unknown.
  module Wiki
  end
end
