## 1. Environment

- Ruby 3.4.1

## 2. Execution

### 2-1. Main

```command
$ cd ./ruby
$ ruby main.rb
==================== Categorizing the Entire github-wiki-organisers Wiki Pages... ====================
========== Organising Home... ==========
Check out An Up-to-date Wiki List on Home at https://github.com/hayat01sh1da/github-wiki-organisers/wiki !!
========== Done Organising Home 🎉 ==========

========== Organising Sidebar... ==========
Check out An Up-to-date Wiki List on Sidebar at https://github.com/hayat01sh1da/github-wiki-organisers/wiki !!
========== Done Organising Home 🎉 ==========
==================== Done Categorizing the Entire github-wiki-organisers Wiki Pages 🎉 ====================
```

## 2-2. Export Unowned Wiki List

```command
$ cd ./ruby
$ ruby export_unowned_wiki_list.rb
==================== Exporting Unowned Wiki List... ====================
Here is the result:

Owner記名なし: 1534件


Check it out result on '../../unowned_wiki_count_list_by_namespace.txt' !!
==================== Done Exporting Unowned Wiki List 🎉 ====================
```

## 3. Bulk Execution of Unit Tests

```command
$ cd ./ruby
$ rake
Run options: --seed 47091

# Running:

....

Finished in 0.375974s, 10.6390 runs/s, 13.2988 assertions/s.

4 runs, 5 assertions, 0 failures, 0 errors, 0 skips
```
