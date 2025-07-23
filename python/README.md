## 1. Environment

- Python 3.13.5

## 2. Execution

Run the commands under `./python`

### 2-1. Options

|Option |Alias        |Usage                                                                                              |
|:------|:------------|:--------------------------------------------------------------------------------------------------|
|`-o`   |`--owner`    |Categorise GitHub Wiki on Home and Sidebar with h2 titles with hyperlinks based on its owner       |
|`-c`   |`--category` |Categorise GitHub Wiki on Home and Sidebar with h2 titles without hyperlinks based on its category |

### 2-2. Update Wiki List on Home and Sidebar

```command
$ python ./exec/update_wiki_list_on_home_and_sidebar.py -o
==================== Categorizing the Entire github-wiki-organisers Wiki Pages... ====================
========== Organising Home... ==========
Check out An Up-to-date Wiki List on Home at https://github.com/hayat01sh1da/github-wiki-organisers/wiki !!
========== Done Organising Home 🎉 ==========

========== Organising Sidebar... ==========
Check out An Up-to-date Wiki List on Sidebar at https://github.com/hayat01sh1da/github-wiki-organisers/wiki !!
==================== Done Categorizing the Entire github-wiki-organisers Wiki Pages 🎉 ====================
========== Done Organising Sidebar 🎉 ==========

==================== Done Categorizing the Entire github-wiki-organisers Wiki Pages 🎉 ====================
```

```command
$ python ./exec/update_wiki_list_on_home_and_sidebar.py -c
==================== Categorizing the Entire github-wiki-organisers Wiki Pages... ====================
========== Organising Home... ==========
Check out An Up-to-date Wiki List on Home at https://github.com/hayat01sh1da/github-wiki-organisers/wiki !!
========== Done Organising Home 🎉 ==========

========== Organising Sidebar... ==========
Check out An Up-to-date Wiki List on Sidebar at https://github.com/hayat01sh1da/github-wiki-organisers/wiki !!
==================== Done Categorizing the Entire github-wiki-organisers Wiki Pages 🎉 ====================
========== Done Organising Sidebar 🎉 ==========

==================== Done Categorizing the Entire github-wiki-organisers Wiki Pages 🎉 ====================
```

## 2-3. Export Unknown Wiki List

```command
$ python ./exec/export_unknown_wiki_count_list_by_namespace.py -o
==================== Exporting Unknown Wiki List... ====================
========== Organising Home... ==========
Here is the result:


Ownerチームが不明だが必要なページ群: 1件
Ownerチーム・要or不要が不明なページ群: 1件
Owner記名なし: 4件


Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!
==================== Done Exporting Unknown Wiki List 🎉 ====================
```

```command
$ python ./exec/export_unknown_wiki_count_list_by_namespace.py -c
==================== Done Exporting Unknown Wiki List 🎉 ====================
01045255@CF4678 python % python ./exec/export_unknown_wiki_count_list_by_namespace.py -c
==================== Exporting Unknown Wiki List... ====================
========== Organising Home... ==========
Here is the result:


Category記載なし: 7件


Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!
==================== Done Exporting Unknown Wiki List 🎉 ====================
```

## 3. Bulk Execution of Unit Tests

```command
$ python -m unittest discover ./test
........................................
----------------------------------------------------------------------
Ran 40 tests in 0.729s

OK
```
