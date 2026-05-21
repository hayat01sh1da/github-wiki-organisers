## 1. Environment

- Ruby 4.0.4

## 2. Install Gems via Gemfile and Bundler

```command
$ bundle install
$ bundle lock --add-checksums
```

## 3. Execution

Run the commands under `./ruby`

### 3-1. Options

| Order | Option        | Input                   |
| :---- | :------------ | :---------------------- |
| 1     | group_by      | `Owner` or `Category`   |
| 2     | language      | `English` or `Japanese` |
| 3     | home_overflow | `true` or `false`       |

### 3-2. Update Wiki List on Home and Sidebar

```command
$ rake update_wiki_list_on_home_and_sidebar
Provide the group_by(Owner or Category)
Owner
Provide the language(English or Japanese)
English
Provide the home_overflow(true or false)
false
-------------------- Categorising the Entire github-wiki-organisers Wiki Pages... --------------------

-------------------- Organising Home... --------------------
Check out an Up-to-date Wiki List on Home at 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki' !!
-------------------- Done Organising Home 🎉 --------------------

-------------------- Organising Sidebar... --------------------
Check out an Up-to-date Wiki List on Sidebar at 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki' !!
-------------------- Done Organising Sidebar 🎉 --------------------

-------------------- Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 --------------------
```

## 3-3. Export Unknown Wiki Count List by Namespace

```command
$ rake export_unknown_wiki_count_list_by_namespace
Provide the group_by(Owner or Category)
Owner
Provide the language(English or Japanese)
English
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Unknown Owner nor Necessity: 1
Unowned but Necessary: 1
Unowned: 10
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 -------------------
```

```command
$ rake export_unknown_wiki_count_list_by_namespace
Provide the group_by(Owner or Category)
Owner
Provide the language(English or Japanese)
Japanese
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Ownerチームが不明だが必要なページ群: 1
Ownerチーム・要or不要が不明なページ群: 1
Owner記名なし: 10
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

### 3-3-2. Category

```command
$ rake export_unknown_wiki_count_list_by_namespace
Provide the group_by(Owner or Category)
Category
Provide the language(English or Japanese)
English
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Uncategorised: 14
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

```command
$ rake export_unknown_wiki_count_list_by_namespace
Provide the group_by(Owner or Category)
Category
Provide the language(English or Japanese)
Japanese
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Category記載なし: 14
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

## 3-4. Export Unknown Wiki List for LLM

```command
$ rake export_unknown_wiki_list_for_llm
Provide the group_by(Owner or Category)
Owner
Provide the language(English or Japanese)
English
-------------------- Exporting Unknown Wiki List... --------------------

Check it out result on '../../export_unknown_wiki_list_for_llm.txt' !!

-------------------- Done Exporting Unknown Wiki List 🎉 --------------------
```

## 4. Unit Tests

```command
$ rake
Run options: --seed 33975

# Running:

............................................................................................................................................................

Finished in 32.985576s, 4.7293 runs/s, 8.7311 assertions/s.

156 runs, 288 assertions, 0 failures, 0 errors, 0 skips
```

## 5. Static Code Analysis

```command
$ rubocop
Inspecting 13 files
.............

13 files inspected, no offenses detected
```

## 6. Type Checks

```command
$ rbs-inline --output sig/generated/ .
🎉 Generated 10 RBS files under sig/generated
# Type checking files:

....................

No type error detected. 🫖
```
