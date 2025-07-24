## 1. Environment

- Ruby 3.4.5

## 2. Execution

Run the commands under `./ruby`

### 2-1. Options

|Option |Alias        |Usage                                                                                              |
|:------|:------------|:--------------------------------------------------------------------------------------------------|
|`-o`   |`--owner`    |Categorise GitHub Wiki on Home and Sidebar with h2 titles with hyperlinks based on its owner       |
|`-c`   |`--category` |Categorise GitHub Wiki on Home and Sidebar with h2 titles without hyperlinks based on its category |

### 2-2. Update Wiki List on Home and Sidebar

```command
$ ruby ./exec/update_wiki_list_on_home_and_sidebar.rb -o
==================== Categorising the Entire github-wiki-organisers Wiki Pages... ====================
========== Organising Home... ==========
Check out an Up-to-date Wiki List on Home at https://github.com/hayat01sh1da/github-wiki-organisers/wiki !!
========== Done Organising Home 🎉 ==========

========== Organising Sidebar... ==========
Check out an Up-to-date Wiki List on Sidebar at https://github.com/hayat01sh1da/github-wiki-organisers/wiki !!
========== Done Organising Home 🎉 ==========
==================== Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 ====================
```

```command
$ ruby ./exec/update_wiki_list_on_home_and_sidebar.rb -c
==================== Categorising the Entire github-wiki-organisers Wiki Pages... ====================
========== Organising Home... ==========
Check out an Up-to-date Wiki List on Home at https://github.com/hayat01sh1da/github-wiki-organisers/wiki !!
========== Done Organising Home 🎉 ==========

========== Organising Sidebar... ==========
Check out an Up-to-date Wiki List on Sidebar at https://github.com/hayat01sh1da/github-wiki-organisers/wiki !!
========== Done Organising Home 🎉 ==========
==================== Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 ====================
```

## 2-3. Export Unknown Wiki List

```command
$ ruby ./exec/export_unknown_wiki_count_list_by_namespace.rb -o
==================== Exporting Unknown Wiki Count List... ====================
Here is the result:

Ownerチームが不明だが必要なページ群: 1件
Ownerチーム・要or不要が不明なページ群: 1件
Owner記名なし: 5件

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!
==================== Done Exporting Unknown Wiki Count List 🎉 ====================
```

```command
$ ruby ./exec/export_unknown_wiki_count_list_by_namespace.rb -c
==================== Exporting Unknown Wiki Count List... ====================
Here is the result:

Category記載なし: 7件

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!
==================== Done Exporting Unknown Wiki Count List 🎉 ====================
```

## 3. Bulk Execution of Unit Tests

```command
$ rake
Run options: --seed 11408

# Running:

..................................

Finished in 0.232616s, 146.1636 runs/s, 245.0390 assertions/s.

34 runs, 57 assertions, 0 failures, 0 errors, 0 skips
```
