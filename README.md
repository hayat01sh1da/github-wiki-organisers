## 1. Common Environment

- WSL(Ubuntu 24.04.1 LTS)

## 2. READMEs

- [Ruby](./ruby/README.md)
- [Python](./python/README.md)

## 3. Source Codes

- [Ruby](./ruby/)
- [Python](./python/)

## 4. How to Use

In any case, make sure that you declare the owner or the category of the Wiki on the top of the document as follows.

```markdown
Owner: @sample-owner

---

This is a sample Wiki.
```

```markdown
Category: sample-category

---

This is a sample Wiki.
```

### 4-1. Edit Wiki

#### 4-1-1. GUI

You can directly create, update and delete wiki pages on [github-wiki-organisers Wiki](https://github.com/quipper/aya-issues/wiki).  
These actions are managed as git commits.

#### 4-1-2. On Your Machine

GitHub Wiki is also managed as git repository, which allows you to use git commands, needless to say.  
Follow the instructions below to edit wiki pages.

1. Run `git clone git@github.com:quipper/aya-issues.git` to clone Wiki.
2. Create, update or delete a wiki and make some differences.
3. Run `git add #{FILENAME}`, `git commit -m #{COMMIT_MESSAGE}` and `git push origin master` in order to push commit(s) to the remote repository.
    - \* The branch you can see on GUI is `master`

⚠️ Make sure that you must not rename and move markdown file on CLI or change the title on GUI in case you lost the revisions.

You can also freely configure Home header passage.  
Edit it on [https://github.com/hayat01sh1da/github-wiki-organisers/blob/master/home_template] based on the mode you are in.

### 4-2. Cron Jobs

#### 4-2-1. Update Wiki List on Home and Sidebar

[Update Wiki List on Home and Sidebar](https://github.com/hayat01sh1da/github-wiki-organisers/actions/workflows/update-wiki-list-on-home-and-sidebar.yml) runs to update wiki list on Home and Sidebar at 12:00 and 22:00 every weekday.  
If there is any difference, it pushes a commit to the remote repository and send a notification to a Slack channel you would like to get information on.  
As a sample, [#github-actions-notifications - hayat01sh1da](https://hayat01sh1da.slack.com/archives/C09BBHZPD5E) is set as the target channel.

> 【github-wiki-organisers Daily Wiki List on Home and Sidebar Update Report】  
> Workflows: [Update Wiki List on Home and Sidebar](https://github.com/hayat01sh1da/github-wiki-organisers/blob/master/.github/workflows/update-wiki-list-on-home-and-sidebar.yml)  
> Commit: 04debbe Update Wiki list on Home and Sidebar by GitHub Actions[bot] at 2025-08-16 15:02:27  
> Source: [github-wiki-organisers Wiki](https://github.com/hayat01sh1da/github-wiki-organisers/wiki)

<img width="624" height="199" alt="Screenshot 2025-08-16 150632" src="https://github.com/user-attachments/assets/a493ef56-3510-4ab0-80ca-9053ee1a237f" />

#### 4-2-2. Notify Unknown Wiki Count by Namespace

[Notify Unknown Wiki Count by Namespace](https://github.com/hayat01sh1da/github-wiki-organisers/actions/workflows/notify-uncategorised-wiki-count-by-namespace.yml) runs to notify unknown wikis in terms of ownership at 10:00 every Monday.  
If there is any difference, it pushes a commit to the remote repository and send a notification to a Slack channel you would like to get information on.  
As a sample, [#github-actions-notifications - hayat01sh1da](https://hayat01sh1da.slack.com/archives/C09BBHZPD5E) is set as the target channel.

> 【github-wiki-organisers Weekly Unowned Wiki Count Report】  
> [Unknown Owner nor Necessity: 1](https://github.com/hayat01sh1da/github-wiki-organisers/wiki#unowned-but-necessary-wiki)  
> [Unowned but Necessary: 1](https://github.com/hayat01sh1da/github-wiki-organisers/wiki#unknown-owner-nor-necessity-wiki)  
> [Unowned: 10](https://github.com/hayat01sh1da/github-wiki-organisers/wiki#unowned)

<img width="540" height="156" alt="Screenshot 2025-08-16 152014" src="https://github.com/user-attachments/assets/2d659efd-06e2-45b2-91f9-e37bb78f50b7" />

#### 4-2-3. Notify Uncategorised Wiki Count by Namespace

[Notify Uncategorised Wiki Count by Namespace](https://github.com/hayat01sh1da/github-wiki-organisers/actions/workflows/notify-uncategorised-wiki-count-by-namespace.yml) runs to notify unknown wikis in terms of category at 10:00 every Monday.  
If there is any difference, it pushes a commit to the remote repository and send a notification to a Slack channel you would like to get information on.  
As a sample, [#github-actions-notifications - hayat01sh1da](https://hayat01sh1da.slack.com/archives/C09BBHZPD5E) is set as the target channel.

> 【github-wiki-organisers Weekly Uncategorised Wiki Count by Namespace Report】  
> [Uncategorised: 14](https://github.com/hayat01sh1da/github-wiki-organisers/wiki#uncategorised)

<img width="516" height="87" alt="Screenshot 2025-08-16 152118" src="https://github.com/user-attachments/assets/639d1d7a-ac7a-42d4-8033-b5f3672d5f3c" />

#### 4-2-4. Export Unknown Wiki List for LLM

[Export Unknown Wiki List for LLM](https://github.com/hayat01sh1da/github-wiki-organisers/actions/workflows/export-unknown-wiki-list-for-llm.yml) runs to notify export of ignored wiki page list for LLM in terms of noise canceling at 0:00 every weekday.  
If there is any difference, it pushes a commit to the remote repository and send a notification to a Slack channel you would like to get information on.  
As a sample, [#github-actions-notifications - hayat01sh1da](https://hayat01sh1da.slack.com/archives/C09BBHZPD5E) is set as the target channel.

Message: The latest ignored page list for LLM has been exported! Make sure if it is as you expect by cloning hayat01sh1da/github-wiki-organisers.wiki !
Workflows: [Export Unknown Wiki List for LLM](https://github.com/hayat01sh1da/github-wiki-organisers/actions/workflows/export-unknown-wiki-list-for-llm.yml)

> 【github-wiki-organisers Wiki LLM Notification for Ignored Page List Export】  
> Message: The latest ignored page list for LLM has been exported! Make sure if it is as you expect by cloning hayat01sh1da/github-wiki-organisers.wiki !  
> Workflows: [Export Unknown Wiki List for LLM](https://github.com/hayat01sh1da/github-wiki-organisers/actions/workflows/export-unknown-wiki-list-for-llm.yml)

<img width="602" height="161" alt="Screenshot 2025-08-16 152957" src="https://github.com/user-attachments/assets/2e425647-50d2-41ae-b953-79a19331ebcf" />
