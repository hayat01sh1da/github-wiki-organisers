# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).  
One repository hosts two packages, so releases are tagged per ecosystem (`ruby-vX.Y.Z` for the RubyGems gem, `python-vX.Y.Z` for the PyPI library).

## [Unreleased]

### 1. Added

- `spreen` CLI with `update`, `count-report` and `llm-export` subcommands plus `--path`, `--group-by`, `--language`, `--overflow`, `--org`, `--repo`, `--wiki-url`, `--template-dir`, `--config`, `--exclude` and `--output` flags, replacing the interactive prompts as the packaged entry point (Ruby and Python).
- `.spreen.yml` config file: sets the organisation/repository (or explicit `wiki_url` / `owner_base_url`), the excluded directories, a custom template directory, and overrides or extends the built-in Owner/Category labels, languages and first-line regexes.
- Ruby gem packaging: `Spreen::Wiki` module under `RubyGem/lib/`, `spreen-wiki.gemspec`, `exe/spreen`, RBS signatures, and the four default Home templates shipped as gem data.
- Python packaging: `spreen_wiki` package under `PyPI/src/`, full PyPI metadata in `pyproject.toml`, `spreen` console script, `py.typed`, and the four default Home templates shipped as package data.
- Configuration tests covering precedence (explicit option > config file > `ORGANISATION_NAME` environment variable > defaults) in both ecosystems.

### 2. Changed

- Renamed the repository to `spreen-wiki` and the ecosystem directories to `RubyGem/` (from `ruby/`) and `PyPI/` (from `python/`).
- Named the packages **`spreen-wiki`** — a blend of the falcon's *stoop* and the *preen* that follows, after Hayato (隼人, "falcon man"): RubyGem `spreen-wiki` (`Spreen::Wiki`), PyPI `spreen-wiki` (`spreen_wiki`), CLI `spreen`, config file `.spreen.yml` (renamed from the working titles `github_wiki_organiser` / `github-wiki-organiser`, CLI `wiki-organise`, `.wiki-organiser.yml`).
- Renamed the Ruby namespace from `Spreen::Wiki` to `SpreenWiki` and the lib path from `lib/spreen/wiki/` to `lib/spreen_wiki/`, matching the Python package's flat `spreen_wiki` layout; `require 'spreen-wiki'`, the gem name and the `spreen` CLI are unchanged.
- Generalised the hardcoded assumptions: the organisation/repository/wiki URL, the owner-team URL, the template path, the scanned base path (now defaulting to the current directory), the excluded directories and the export filenames are all configuration, with the previous behaviour preserved as defaults.
- Owner headings degrade gracefully to unlinked text when no organisation is configured instead of linking to a hardcoded personal account.
- The wiki cron workflows pass `ORGANISATION_NAME` from `github.repository_owner` and keep driving the (unchanged) interactive Rake task interface.
- Fixed `README.md` § 4-1-2: the wiki clone instruction pointed at an unrelated repository; now points at this repository's wiki.

### 3. Removed

- Flat `ruby/src/` and `PyPI/src/` script layouts (superseded by the gem and
  package layouts above).
