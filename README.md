# Praise Audit: Results

This repository contains the results of the praise audit performed during February 2022. It was set in motion because of [this issue](https://github.com/CommonsBuild/coordination/issues/1142
), where a community member noticed that his praise messages weren't being reacted to by the praise bot. 
It was therefore decided to take a closer look at the praise dished during a shorter period of time (in this case 01. November 2021 - 31. January 2022) to gauge the size of the issue. 

For this analysis @Vyvy-vi generously supplied the following files:
- **GoogleDiscord Praise Bot Sheet - Sheet1.csv** : This is a copy of the "official" praise sheet hosted on drive.google..... It contains all data since June and is used as "source of truth" during quantification. The goal was to see which praise (if any) DIDN'T end up here.

- **Token_Engineering_Commons_praise_2.csv**: A scrape of all the !praise dished in the TEC Discord server.

- **praise_samples_810180621930070088_1.json** : The same as above, but in JSON format also saving reactions to the messages (for example the ✅ from the bot).

After taking a first look at the data it became clear very quickly that a missing ✅ in the discord channel didn't necessarily result in a missing entry in the Google Document, so we only ended up using the first two files for our analysis. The plan of action was:
- Discard praise outside of the specifed dates
- Join both datasets by giver, receiver and date, keeping the rest of the information as separate columns for review. 
- Output a table with all instances of praise which were preent in one file and not in the other. 

The code used can be found in `combine_praise_datasets.py`

We generated two files: `joined_dataset.csv`, with the whole matching table
and `only_incomplete.csv`, with only those praise instances which couldn't be directly matched. 

A glance into `only_incomplete.csv` shows a that for most cases, the "unmatched" praises had been correctly saved, but due to the user having a server-specific name (like "griff (💜, 💜)#8888") they weren't being correctly attributed by our script to the equivalent in the google spreadsheet, which saves the "real" username.

As a result, some of the most common users were substituted in the python code, the rest were adjusted manually in the file `UnmatchedPraise_ManualRevision.csv` by adding an "X" in the last column if the praise was matched elsewhere and as such not faulty.

The final table with all the "real" missed praise is `final_edge_cases.csv`

In that file, there is a total of around 55 "edge cases" (out of nearly 20,000) where praise wasn't saved. 
It's important to note that an "unsaved praise" does not necessarily correspond to a "bug" in the praise bot, since there are legitimate reasons for praise to not be counted, as:
- The user didn't have praise power at the moment they dished praise. 
- The praise was edited. If a user adds a mention to a praise as an edit instead of posting it as a new message, it doesn't get picked up by the bot.

The first one probably accounts for most of the singletons. Taking a look at the praise reasons you can find several mentions to onboarding, or praise by known community members from around the time they joined (but not later!).

With those caveats in mind **it still looks like some particular instances of praise were accidentally dropped**. 

# What to do now
The main takeaway from the audit is: Most of the praise was correctly saved, and only the checkmark reaction in the discord channel turned out to be inconsistent.

Given the very small number of "buggy" praise and the fact that going forward we are going to use a new praise bot anyway, we would argue that a thorough review of the historical praise data before the retroactive quantifications is not merited. We suggest using the existing google spreadsheet as is.

