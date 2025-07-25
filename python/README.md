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
$ python ./exec/update_wiki_list_on_home_and_sidebar.py -c
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
$ python ./exec/export_unknown_wiki_count_list_by_namespace.py -o
==================== Exporting Unknown Wiki Count List... ====================
Here is the result:

Unknown Owner nor Necessity: 1
Unowned but Necessary: 1
Unowned: 5

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!
==================== Done Exporting Unknown Wiki Count List 🎉 ====================
```

```command
$ python ./exec/export_unknown_wiki_count_list_by_namespace.py -c
==================== Exporting Unknown Wiki Count List... ====================
Here is the result:

Uncategorised: 7

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!
==================== Done Exporting Unknown Wiki Count List 🎉 ====================
```

## 3. Bulk Execution of Unit Tests

```command
$ python -m unittest discover ./test
........................................
----------------------------------------------------------------------
Ran 40 tests in 0.729s

OK
```
