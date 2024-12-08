## 1. Environment

- Python 3.13.1

## 2. Execution

```command
$ cd ./python
$ python main.py 
==================== Categorizing the Entire aya-issues Wiki Pages... ====================
========== Tidying Directories... ==========
===== Making Directories by Owner Unit... =====
../../test-owner
../../Ownerチームが不明だが必要なページ群
../../Ownerチーム・要or不要が不明なページ群
../../Owner記名なし
===== Done Making Directories by Owner Unit 🎉 =====

===== Moving Files to Owner's Directories... =====
../../Owner記名ありページ.md => ../../test-owner/Owner記名ありページ.md
../../Ownerチームが不明だが必要なページ.md => ../../Ownerチームが不明だが必要なページ群/Ownerチームが不明だが必要なページ.md
../../Ownerチーム・要or不要が不明なページ.md => ../../Ownerチーム・要or不要が不明なページ群/Ownerチーム・要or不要が不明なページ.md
../../Owner記名なしページ1.md => ../../Owner記名なし/Owner記名なしページ1.md
../../Owner記名なしページ2.md => ../../Owner記名なし/Owner記名なしページ2.md
===== Done Moving Files to Owner's Directories 🎉 =====

===== Deleting Empty Directories... =====
===== Done Deleting Empty Directories 🎉 =====
========== Done Tidying Directories 🎉 ==========

========== Tidying Home... ==========
Check out An Up-to-date Wiki List on Home at https://github.com/quipper/aya-issues/wiki !!
========== Done Tidying Home 🎉 ==========

========== Tidying Sidebar... ==========
Check out An Up-to-date Wiki List on Sidebar at https://github.com/quipper/aya-issues/wiki !!
========== Done Tidying Home 🎉 ==========
==================== Done Categorizing the Entire aya-issues Wiki Pages 🎉 ====================
```

## 3. Bulk Execution of Unit Tests

```command
$ cd ./python
$ python -m unittest discover ./test
.......
----------------------------------------------------------------------
Ran 7 tests in 0.326s

OK
```
