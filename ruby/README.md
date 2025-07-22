## 1. Environment

- Ruby 3.4.5

## 2. Execution

### 2-1. Update Wiki List on Home and Sidebar

```command
$ cd ./ruby
$ ruby ./exec/update_wiki_list_on_home_and_sidebar.rb
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
$ ruby ./exec/export_unowned_wiki_list.rb
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
$ cd ./ruby
$ rake
Run options: --seed 64243

# Running:

.........

Finished in 0.781830s, 11.5115 runs/s, 14.0696 assertions/s.

9 runs, 11 assertions, 0 failures, 0 errors, 0 skips
```
