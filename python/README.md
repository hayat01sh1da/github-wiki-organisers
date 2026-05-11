## 1. Environment

- Python 3.14.5

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

Run the commands under `./python`

### 3-1. Options

| Order | Option        | Command-line Argument   |
| :---- | :------------ | :---------------------- |
| 1     | group_by      | `Owner` or `Category`   |
| 2     | language      | `English` or `Japanese` |
| 3     | home_overflow | `True` or `False`       |

### 3-2. Update Wiki List on Home and Sidebar

```command
$ python exec/update_wiki_list_on_home_and_sidebar.py Owner English
-------------------- Categorising the Entire github-wiki-organisers Wiki Pages... --------------------

-------------------- Organising Home... --------------------
Check out an Up-to-date Wiki List on Home at 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki' !!
-------------------- Done Organising Home 🎉 --------------------

-------------------- Organising Sidebar... --------------------
Check out an Up-to-date Wiki List on Sidebar at 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki' !!
-------------------- Done Organising Sidebar 🎉 --------------------

-------------------- Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 ---------------------
```

## 3-3. Export Unknown Wiki Count List by Namespace

### 3-3-1. Owner

```command
$ python exec/export_unknown_wiki_count_list_by_namespace.py Owner English
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Unknown Owner nor Necessity: 1
Unowned but Necessary: 1
Unowned: 14
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

```command
$ python exec/export_unknown_wiki_count_list_by_namespace.py Owner Japanese
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Ownerチームが不明だが必要なページ群: 1
Ownerチーム・要or不要が不明なページ群: 1
Owner記名なし: 14
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

### 3-3-2. Category

```command
$ python exec/export_unknown_wiki_count_list_by_namespace.py Category English
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Uncategorised: 18
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

```command
$ python exec/export_unknown_wiki_count_list_by_namespace.py Category Japanese
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Category記載なし: 18
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

## 3-4. Export Unknown Wiki List for LLM

```command
$ python exec/export_unknown_wiki_list_for_llm.py
-------------------- Exporting Unknown Wiki List... --------------------

Check it out result on '../../export_unknown_wiki_list_for_llm.txt' !!

-------------------- Done Exporting Unknown Wiki List 🎉 --------------------
```

## 4. Bulk Execution of Unit Tests

```command
$ pytest
====================================================================== test session starts =======================================================================
platform linux -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: /mnt/c/Users/binlh/Documents/development/github-wiki-organisers/python
collected 148 items                                                                                                                                              

test/test_application.py ....                                                                                                                              [  2%]
test/test_home.py ................................                                                                                                         [ 24%]
test/test_sidebar.py ........................                                                                                                              [ 40%]
test/test_unknown_wiki_count_list_exporter.py ................................................................                                             [ 83%]
test/test_unknown_wiki_list_exporter_for_llm.py ........................                                                                                   [100%]

====================================================================== 148 passed in 12.44s ======================================================================
```
