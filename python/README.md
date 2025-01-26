## 1. Environment

- Python 3.13.1

## 2. Execution

### 2-1. Main

```command
$ cd ./python
$ python main.py
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
========== Organising Home... ==========
Here is the result:


# infer-owner: 1件
Owner記名なし: 1535件


Check it out result on '../../unowned_wiki_count_list_by_namespace.txt' !!
==================== Done Exporting Unowned Wiki List 🎉 ====================
```

## 3. Bulk Execution of Unit Tests

```command
$ cd ./python
$ python -m unittest discover ./test
.......
----------------------------------------------------------------------
Ran 7 tests in 0.040s

OK
```
