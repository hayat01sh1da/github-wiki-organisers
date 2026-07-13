[![Actions Status: Python - CI](https://github.com/hayat01sh1da/github-wiki-organisers/workflows/Python%20-%20CI/badge.svg)](https://github.com/hayat01sh1da/github-wiki-organisers/actions?query=workflow%3A%22Python%20-%20CI%22)
[![Actions Status: Python - Daily Dependencies Update](https://github.com/hayat01sh1da/github-wiki-organisers/workflows/Python%20-%20Daily%20Dependencies%20Update/badge.svg)](https://github.com/hayat01sh1da/github-wiki-organisers/actions?query=workflow%3A%22Python%20-%20Daily%20Dependencies%20Update%22)
[![Actions Status: Ruby - CI](https://github.com/hayat01sh1da/github-wiki-organisers/workflows/Ruby%20-%20CI/badge.svg)](https://github.com/hayat01sh1da/github-wiki-organisers/actions?query=workflow%3A%22Ruby%20-%20CI%22)
[![Actions Status: Ruby - Daily Dependencies Update](https://github.com/hayat01sh1da/github-wiki-organisers/workflows/Ruby%20-%20Daily%20Dependencies%20Update/badge.svg)](https://github.com/hayat01sh1da/github-wiki-organisers/actions?query=workflow%3A%22Ruby%20-%20Daily%20Dependencies%20Update%22)
[![Actions Status: Export Unknown Wiki List for LLM](https://github.com/hayat01sh1da/github-wiki-organisers/workflows/Export%20Unknown%20Wiki%20List%20for%20LLM/badge.svg)](https://github.com/hayat01sh1da/github-wiki-organisers/actions?query=workflow%3A%22Export%20Unknown%20Wiki%20List%20for%20LLM%22)
[![Actions Status: Notify Uncategorised Wiki Count by Namespace](https://github.com/hayat01sh1da/github-wiki-organisers/workflows/Notify%20Uncategorised%20Wiki%20Count%20by%20Namespace/badge.svg)](https://github.com/hayat01sh1da/github-wiki-organisers/actions?query=workflow%3A%22Notify%20Uncategorised%20Wiki%20Count%20by%20Namespace%22)
[![Actions Status: Notify Unknown Wiki Count by Namespace](https://github.com/hayat01sh1da/github-wiki-organisers/workflows/Notify%20Unknown%20Wiki%20Count%20by%20Namespace/badge.svg)](https://github.com/hayat01sh1da/github-wiki-organisers/actions?query=workflow%3A%22Notify%20Unknown%20Wiki%20Count%20by%20Namespace%22)
[![Actions Status: Update Wiki List on Home and Sidebar](https://github.com/hayat01sh1da/github-wiki-organisers/workflows/Update%20Wiki%20List%20on%20Home%20and%20Sidebar/badge.svg)](https://github.com/hayat01sh1da/github-wiki-organisers/actions?query=workflow%3A%22Update%20Wiki%20List%20on%20Home%20and%20Sidebar%22)
[![Actions Status: CodeQL](https://github.com/hayat01sh1da/github-wiki-organisers/workflows/CodeQL/badge.svg)](https://github.com/hayat01sh1da/github-wiki-organisers/actions?query=workflow%3A%22CodeQL%22)

# spreen-wiki

Organises a GitHub wiki: generates `Home.md` and `_Sidebar.md` by grouping the pages by the **Owner** or **Category** declared on the first line of each page (English and Japanese labels built in, extensible via a config file), and exports reports of the pages whose owner or category is unknown.

The name blends the falcon's **stoop** and the **preen** that follows — a falconet at work, after Hayato (隼人, "falcon man").  
The tool ships twice with identical behaviour: as the RubyGems gem **`spreen-wiki`** and as the PyPI library **`spreen-wiki`**.  Both install the same `spreen` command.

## 1. Quickstart

Install one of the two implementations:

```command
$ gem install spreen-wiki
```

```command
$ pipx install spreen-wiki
```

Clone your repository's wiki, declare an owner (or category) on the first line of each page, and run the organiser:

```command
$ git clone git@github.com:<org>/<repo>.wiki.git
$ cd <repo>.wiki
$ spreen update --path . --org <org> --repo <repo>
Updated Home.md and _Sidebar.md.
Check them out at 'https://github.com/<org>/<repo>/wiki' !!
$ git add Home.md _Sidebar.md && git commit -m 'Organise wiki' && git push origin master
```

The other two commands export reports about the pages whose owner/category is still unknown:

```command
$ spreen count-report --path . # counts per unknown namespace
$ spreen llm-export --path .   # flat page list to feed to an LLM
```

Run `spreen <command> --help` for the full flag list (`--group-by`, `--language`, `--overflow`, `--template-dir`, `--exclude`, `--output`, ...).

## 2. Wiki Page Convention

Declare the owner or the category of every wiki page on the top line of the document as follows.

```markdown
Owner: @sample-owner

---

This is a sample Wiki.
```

```markdown
Category: sample-category

---

This is a sample Wiki.
```

Pages without a declaration are collected under the "Unowned" / "Uncategorised" namespace (`Owner記名なし` / `Category記載なし` in Japanese) so they stay visible until someone claims them.

## 3. Configuration

Every hardcoded assumption of the original tool is now configurable. Values are resolved with the same precedence everywhere: **explicit CLI flag / keyword argument → `.spreen.yml` → `ORGANISATION_NAME` environment variable (organisation only) → built-in default**.

Place a `.spreen.yml` at the root of the wiki clone (or point at one with `--config`):

```yaml
# Used to build the wiki URL and the owner-team links. Equivalent to
# --org/--repo; omit them and set wiki_url/owner_base_url directly if your
# links do not follow the github.com defaults.
organisation: my-org
repository: my-repo
# wiki_url: https://github.com/my-org/my-repo/wiki
# owner_base_url: https://github.com/orgs/my-org/teams/

# Directories skipped while scanning (default below). Keep wikis-by-owner in
# the list when you use `update --overflow`, which writes into it.
exclude:
  - github-wiki-organisers
  - wikis-by-owner

# Where the Home header templates live, as <group_by>/<language>.md
# (e.g. owner/english.md). Defaults to the templates shipped with the package.
# template_dir: ./my_templates

# Override or extend the built-in labels: change the first-line regexp, add
# languages, or add whole group_by criteria. Anything not listed here keeps
# its built-in value.
labels:
  Owner:
    # regexp: '[Oo]wner:\s?'
    languages:
      French:
        no_declaration: Sans propriétaire        # namespace for undeclared pages
        unknown_namespaces:                      # namespaces in count-report
          - Sans propriétaire
        llm_target_namespace: Sans propriétaire  # namespace llm-export dumps
```

When no organisation is configured at all, owner headings are rendered without team links instead of failing.

## 4. GitHub Actions Reference Implementations

The point of the organiser is automation: this repository runs it on its own wiki with cron workflows you can copy into your repository.  
They check out the wiki, run the organiser, commit and push when there is a diff, and notify a Slack channel (as a sample, [#github-actions-notifications - hayat01sh1da](https://hayat01sh1da.slack.com/archives/C09BBHZPD5E) is set as the target channel).

### 4-1. Update Wiki List on Home and Sidebar

[update-wiki-list-on-home-and-sidebar.yml](./.github/workflows/update-wiki-list-on-home-and-sidebar.yml) regenerates Home and Sidebar at 12:00 and 22:00 JST every weekday.

> 【github-wiki-organisers Daily Wiki List on Home and Sidebar Update Report】
> Workflows: [Update Wiki List on Home and Sidebar](https://github.com/hayat01sh1da/github-wiki-organisers/blob/master/.github/workflows/update-wiki-list-on-home-and-sidebar.yml)
> Commit: 04debbe Update Wiki list on Home and Sidebar by GitHub Actions[bot] at 2025-08-16 15:02:27
> Source: [github-wiki-organisers Wiki](https://github.com/hayat01sh1da/github-wiki-organisers/wiki)

<img width="624" height="199" alt="Screenshot 2025-08-16 150632" src="https://github.com/user-attachments/assets/a493ef56-3510-4ab0-80ca-9053ee1a237f" />

### 4-2. Notify Wiki Count by Namespace

[notify-wiki-count-by-namespace.yml](./.github/workflows/notify-wiki-count-by-namespace.yml) reports the unknown-owner and uncategorised counts at 09:00 JST every Monday.

> 【github-wiki-organisers Weekly Unowned Wiki Count Report】
> [Unknown Owner nor Necessity: 1](https://github.com/hayat01sh1da/github-wiki-organisers/wiki#unowned-but-necessary-wiki)
> [Unowned but Necessary: 1](https://github.com/hayat01sh1da/github-wiki-organisers/wiki#unknown-owner-nor-necessity-wiki)
> [Unowned: 10](https://github.com/hayat01sh1da/github-wiki-organisers/wiki#unowned)

<img width="540" height="156" alt="Screenshot 2025-08-16 152014" src="https://github.com/user-attachments/assets/2d659efd-06e2-45b2-91f9-e37bb78f50b7" />

> 【github-wiki-organisers Weekly Uncategorised Wiki Count by Namespace Report】
> [Uncategorised: 14](https://github.com/hayat01sh1da/github-wiki-organisers/wiki#uncategorised)

<img width="516" height="87" alt="Screenshot 2025-08-16 152118" src="https://github.com/user-attachments/assets/639d1d7a-ac7a-42d4-8033-b5f3672d5f3c" />

### 4-3. Export Unknown Wiki List for LLM

[export-unknown-wiki-list-for-llm.yml](./.github/workflows/export-unknown-wiki-list-for-llm.yml) exports the ignored page list for LLM noise-cancelling at 00:00 JST every weekday.

> 【github-wiki-organisers Wiki LLM Notification for Ignored Page List Export】
> Message: The latest ignored page list for LLM has been exported! Make sure if it is as you expect by cloning hayat01sh1da/github-wiki-organisers.wiki !
> Workflows: [Export Unknown Wiki List for LLM](https://github.com/hayat01sh1da/github-wiki-organisers/actions/workflows/export-unknown-wiki-list-for-llm.yml)

<img width="602" height="161" alt="Screenshot 2025-08-16 152957" src="https://github.com/user-attachments/assets/2e425647-50d2-41ae-b953-79a19331ebcf" />

## 5. Editing This Repository's Wiki

### 5-1. GUI

You can directly create, update and delete wiki pages on [github-wiki-organisers Wiki](https://github.com/hayat01sh1da/github-wiki-organisers/wiki).  
These actions are managed as git commits.

### 5-2. On Your Machine

GitHub Wiki is also managed as a git repository, which allows you to use git commands, needless to say.  
Follow the instructions below to edit wiki pages.

1. Run `git clone git@github.com:hayat01sh1da/github-wiki-organisers.wiki.git` to clone this repository's Wiki.
2. Create, update or delete a wiki and make some differences.
3. Run `git add #{FILENAME}`, `git commit -m #{COMMIT_MESSAGE}` and `git push origin master` in order to push commit(s) to the remote repository.
    - \* The branch you can see on GUI is `master`

⚠️ Make sure that you must not rename and move markdown file on CLI or change the title on GUI in case you lost the revisions.

You can also freely configure the Home header passage this repository's cron jobs use.
Edit it on [./home_template/](https://github.com/hayat01sh1da/github-wiki-organisers/blob/master/home_template) based on the mode you are in. (Package consumers get the same defaults shipped with the package and override them with `template_dir`.)

## 6. Development

- Common environment: WSL (Ubuntu 25.10)
- [Ruby implementation](./ruby/README.md) — gem sources under [./ruby/](./ruby/)
- [Python implementation](./python/README.md) — package sources under [./python/](./python/)
- Release notes live in [CHANGELOG.md](./CHANGELOG.md)
