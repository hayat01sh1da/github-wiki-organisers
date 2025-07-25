## 1. Environment

- Python 3.13.5

## 2. Execution

Run the commands under `./python`

### 2-1. Options

|Order |Option   |Command-line Argument               |
|:-----|:--------|:-----------------------------------|
|1     |genre    |`-o` `--owner` or `-c` `--category` |
|2     |language |`-en` or `-ja`                      |

### 2-2. Update Wiki List on Home and Sidebar

```command
$ python exec/update_wiki_list_on_home_and_sidebar.py -o -en
-------------------- Categorising the Entire github-wiki-organisers Wiki Pages... --------------------

-------------------- Organising Home... --------------------
Check out an Up-to-date Wiki List on Home at 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki' !!
-------------------- Done Organising Home 🎉 --------------------

-------------------- Organising Sidebar... --------------------
Check out an Up-to-date Wiki List on Sidebar at 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki' !!
-------------------- Done Organising Sidebar 🎉 --------------------

-------------------- Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 ---------------------
```

## 2-3. Export Unknown Wiki Count List by Namespace

### 2-3-1. Owner

```command
$ python exec/export_unknown_wiki_count_list_by_namespace.py -o -en
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
$ python exec/export_unknown_wiki_count_list_by_namespace.py -o -ja
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

### 2-3-2. Category

```command
$ python exec/export_unknown_wiki_count_list_by_namespace.py -c -en
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Uncategorised: 18
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

```command
$ python exec/export_unknown_wiki_count_list_by_namespace.py -c -ja
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Category記載なし: 18
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

## 3. Bulk Execution of Unit Tests

```command
$ python -m unittest discover ./test
.......................................................................................
----------------------------------------------------------------------
Ran 87 tests in 5.292s

OK
```
