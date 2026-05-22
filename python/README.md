## 1. Environment

- Python 3.14.5

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

Run the commands under `./python`

### 3-1. Update Wiki List on Home and Sidebar

```command
$ python ./exec/update_wiki_list_on_home_and_sidebar.py
Provide the group_by(Owner or Category): Owner
Provide the language(English or Japanese): English
Provide the home_overflow(true or false): false
-------------------- Categorising the Entire github-wiki-organisers Wiki Pages... --------------------

-------------------- Organising Home... --------------------
Check out an Up-to-date Wiki List on Home at 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki' !!
-------------------- Done Organising Home 🎉 --------------------

-------------------- Organising Sidebar... --------------------
Check out an Up-to-date Wiki List on Sidebar at 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki' !!
-------------------- Done Organising Sidebar 🎉 --------------------

-------------------- Done Categorising the Entire github-wiki-organisers Wiki Pages 🎉 --------------------
```

## 3-2. Export Unknown Wiki Count List by Namespace

### 3-2-1. Owner

```command
$ python ./exec/export_unknown_wiki_count_list_by_namespace.py
Provide the group_by(Owner or Category): Owner
Provide the language(English or Japanese): English
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
$ python ./exec/export_unknown_wiki_count_list_by_namespace.py
Provide the group_by(Owner or Category): Owner
Provide the language(English or Japanese): Japanese
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

### 3-2-2. Category

```command
$ python ./exec/export_unknown_wiki_count_list_by_namespace.py
Provide the group_by(Owner or Category): Category
Provide the language(English or Japanese): English
-------------------- Exporting Unknown Wiki Count List... --------------------

Here is the result:

---------------------------------------
Uncategorised: 14
---------------------------------------

Check it out result on '../../unknown_wiki_count_list_by_namespace.txt' !!

-------------------- Done Exporting Unknown Wiki Count List 🎉 --------------------
```

```command
$ python ./exec/export_unknown_wiki_count_list_by_namespace.py
Provide the group_by(Owner or Category): Category
Provide the language(English or Japanese): Japanese
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
$ python ./exec/export_unknown_wiki_list_for_llm.py
Provide the group_by(Owner or Category): Owner
Provide the language(English or Japanese): English
-------------------- Exporting Unknown Wiki List... --------------------

Check it out result on '../../export_unknown_wiki_list_for_llm.txt' !!

-------------------- Done Exporting Unknown Wiki List 🎉 --------------------
```

## 4. Unit Tests

```command
$ pytest .
============================= test session starts ==============================
platform linux -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: github-wiki-organisers/python
configfile: pyproject.toml
collected 32 items

test/test_application.py ....                                            [ 12%]
test/test_home.py ......                                                 [ 31%]
test/test_sidebar.py ....                                                [ 43%]
test/test_unknown_wiki_count_list_exporter.py ..............             [ 87%]
test/test_unknown_wiki_list_exporter_for_llm.py ....                     [100%]

============================== 32 passed in 3.39s ==============================
```

## 5. Static Code Analysis

```command
$ flake8 .
./exec/export_unknown_wiki_count_list_by_namespace.py:15:80: E501 line too long (87 > 79 characters)
./exec/export_unknown_wiki_count_list_by_namespace.py:27:80: E501 line too long (91 > 79 characters)
./exec/export_unknown_wiki_list_for_llm.py:15:80: E501 line too long (81 > 79 characters)
./exec/export_unknown_wiki_list_for_llm.py:20:80: E501 line too long (85 > 79 characters)
./exec/update_wiki_list_on_home_and_sidebar.py:17:80: E501 line too long (111 > 79 characters)
./exec/update_wiki_list_on_home_and_sidebar.py:29:80: E501 line too long (115 > 79 characters)
./src/application.py:50:80: E501 line too long (80 > 79 characters)
./src/unknown_wiki_count_list_exporter.py:26:80: E501 line too long (80 > 79 characters)
./test/conftest.py:15:80: E501 line too long (84 > 79 characters)
./test/test_application.py:30:80: E501 line too long (92 > 79 characters)
./test/test_application.py:41:80: E501 line too long (107 > 79 characters)
./test/test_home.py:44:80: E501 line too long (109 > 79 characters)
./test/test_home.py:79:80: E501 line too long (84 > 79 characters)
./test/test_home.py:80:80: E501 line too long (114 > 79 characters)
./test/test_home.py:165:80: E501 line too long (91 > 79 characters)
./test/test_home.py:192:80: E501 line too long (87 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:20:80: E501 line too long (88 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:27:80: E501 line too long (100 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:29:80: E501 line too long (92 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:30:80: E501 line too long (104 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:34:80: E501 line too long (100 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:37:80: E501 line too long (92 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:41:80: E501 line too long (102 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:44:80: E501 line too long (104 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:48:80: E501 line too long (102 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:51:80: E501 line too long (92 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:52:80: E501 line too long (104 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:54:80: E501 line too long (102 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:69:80: E501 line too long (92 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:70:80: E501 line too long (104 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:90:80: E501 line too long (96 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:92:80: E501 line too long (84 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:93:80: E501 line too long (88 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:97:80: E501 line too long (96 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:100:80: E501 line too long (84 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:104:80: E501 line too long (98 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:107:80: E501 line too long (88 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:111:80: E501 line too long (98 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:114:80: E501 line too long (84 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:115:80: E501 line too long (88 > 79 characters)
./test/test_unknown_wiki_count_list_exporter.py:117:80: E501 line too long (98 > 79 characters)
$ autoflake8 --in-place --remove-duplicate-keys --remove-unused-variables --recursive .
$ autopep8 --in-place --aggressive --aggressive --recursive .
```

## 6. Type Checks

```command
$ mypy .
Success: no issues found in 14 source files
```
