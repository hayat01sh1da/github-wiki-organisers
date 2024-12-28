## 1. Environment

- Ruby 3.4.1

## 2. Execution

```command
$ cd ./ruby
$ ruby main.rb 
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
$ cd ./ruby
$ rake
Run options: --seed 29933

# Running:

....

Finished in 31.046599s, 0.1288 runs/s, 0.3221 assertions/s.

4 runs, 10 assertions, 0 failures, 0 errors, 0 skips
```
