## 1. Environment

- Ruby 3.4.5

## 2. Execution

Run the commands under `./ruby`

### 2-1. Options

|Order |Option   |Command-line Argument               |
|:-----|:--------|:-----------------------------------|
|1     |group_by |`-o` `--owner` or `-c` `--category` |
|2     |language |`-en` or `-ja`                      |

### 2-2. Update Wiki List on Home and Sidebar

```command
$ ruby exec/update_wiki_list_on_home_and_sidebar.rb
-------------------- Categorising the Entire github-wiki-organisers Wiki Pages... --------------------

-------------------- Organising Home... --------------------
Check out an Up-to-date Wiki List on Home at 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki' !!
-------------------- Done Organising Home 🎉 --------------------

-------------------- Organising Sidebar... --------------------
Check out an Up-to-date Wiki List on Sidebar at 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki' !!
-------------------- Done Organising Sidebar 🎉 --------------------

-------------------- Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 --------------------
```

## 2-3. Export Unknown Wiki Count List by Namespace

```command
$ ruby exec/export_unknown_wiki_count_list_by_namespace.rb -o -en
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
$ ruby exec/export_unknown_wiki_count_list_by_namespace.rb -o -ja
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

### 2-3-2. Category

```command
$ ruby exec/export_unknown_wiki_count_list_by_namespace.rb -c -en
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Uncategorised: 14
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

```command
$ ruby exec/export_unknown_wiki_count_list_by_namespace.rb -c -ja
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Category記載なし: 14
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

## 2-4. Export Unknown Wiki List for LLM 

```command
$ ruby exec/export_unknown_wiki_list_for_llm.rb
-------------------- Exporting Unknown Wiki List... --------------------

Check it out result on '../../export_unknown_wiki_list_for_llm.txt' !!

-------------------- Done Exporting Unknown Wiki List 🎉 --------------------
```

## 3. Bulk Execution of Unit Tests

```command
$ rake
Run options: --seed 33318

# Running:

.........................................................................................................

Finished in 0.579480s, 181.1969 runs/s, 317.5261 assertions/s.

105 runs, 184 assertions, 0 failures, 0 errors, 0 skips
```
