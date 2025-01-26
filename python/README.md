## 1. Environment

- Python 3.13.1

## 2. Execution

### 2-1. Update Wiki List on Home and Sidebar

```command
$ cd ./python
$ python update_wiki_list_on_home_and_sidebar.py
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

## 2-2. Export Unowned Wiki List

```command
$ cd ./python
$ python export_unowned_wiki_list.py
==================== Exporting Unowned Wiki List... ====================
Here is the result:

Ownerチームが不明だが必要なページ群: 13件
Ownerチーム・要or不要が不明なページ群: 209件
Owner記名なし: 0件

Check it out result on '../../unowned_wiki_count_list_by_namespace.txt' !!
==================== Done Exporting Unowned Wiki List 🎉 ====================
```

## 3. Bulk Execution of Unit Tests

```command
$ cd ./python
$ python -m unittest discover ./test
............
----------------------------------------------------------------------
Ran 12 tests in 0.087s

OK
```
