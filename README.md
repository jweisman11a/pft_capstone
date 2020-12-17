# NBCSports PFT Article Recommender

This project is intended to serve as my Deloitte Machine Learning  Guild (MLG) capstone project during Fall 2020/Spring 2021. The completed project is due NLT March 2021 with the primary code review performed in December 2020.

| Project Role  | Name |
| ------------- | ------------- |
| Apprentice  | [Jeff Weisman](https://github.com/jweisman11a)  |
| Master  | [George Panteras](https://github.com/GPanoptis)  |


### Project Idea

Website: https://profootballtalk.nbcsports.com/

![NBCSport's ProFootballTalk](assets/pft_logo.png)


Football fans know a lot of newsworthy events and stories happen every day, even more so during the season and around playoffs/SB. Most casual fans and even some avid fans don't always have enough time to read through all the articles written every day. To help readers who want to stay up on the latest news and stories about the people and events they care about, I am going to build an article recommender. The recommender will take into account the specific level of engagement of each commentor and the kinds of the articles they engage with to determine how many and which articles to recommend.


### Data

There are two sources of data for this project: articles and comments

**Articles are comprised of:**
- Title
- URL (unique)
- Author name
- Posted datetime
- Body (unstructured text)
- \# of comments

**Comments are comprised of:**
- Username
- Posted datetime
- Comment
- \# of likes and dislikes

Sample article: https://profootballtalk.nbcsports.com/2020/12/16/rams-favored-by-17-over-jets/


### Collecting existing articles and comments

In order to start the project, I need to confirm I'm able to collect all the articles and comments from the PFT website since the sites inception. According to [this article](https://profootballtalk.nbcsports.com/2007/10/24/about/), Profootballtalk.com was launched in 2001 but the Rumor Mill (which contains the articles I'm interested in) only has articles going back to October 2007.

It appears the Rumor Mill contains ~15 articles/page and at the moment of this writing, has 13,503 pages. That means there are approximately 202,545 articles to collect. Assuming articles average of ~5 comments/article, that means there are approximately 1,012,725 comments to collect.^

^Estimate was off -> there are 5.6 million comments

To test this, I need to complete the following tasks:

- [x] Write a function to scrape a single article including the 6 elements above
- [x] Write a function to scrape comments from a single article including the 4 elements above
- [x] Push code to the repo
- [x] Submit to MLG pod team members for review and feedback

Now that I have some basic functions to scrape the data, let's look at what's next. Since I expect there to be >200k articles and 5x as many comments, I need both functions to be fairly efficient. Let's see if we can thread one or both functions before we begin our full data collect.

- [x] Write code to leverage multiprocessing library to speed up article collection
- [x] Write code to leverage multiprocessing library to speed up comment collection (currently very slow)

Now that is complete, it's time to collect our data!

- [x] Collect all articles
- [x] Collect all comments


### EDA

EDA is a critical stage in any data science project. My main objectives for this stage are:

1. Understand my data and what it contains
2. Cleanse my data as needed
3. Analyze the relationships between my data elements

Since one can spend a near endless amount of time performing EDA, let's define some core tasks for what needs to be accomplished for each of our two datasets:

**Articles EDA**
- [x] Inspect for correct data types
- [x] Remove records collected incorrectly
- [x] Clean fields
- [x] Check each column for uniqueness, statistical properties, outliers
- [x] Generate plots
- [x] NLP specific tasks (word freq, sentence length, avg word length, stopwords, readability)
https://neptune.ai/blog/exploratory-data-analysis-natural-language-processing-tools

**Comments EDA**
-  [ ] TBD


### Identify commentor engagement using Clustering

Now that I have a basic understanding of the data, I want to analyze the commentors to identify whether there are groups of users with similar behaviors (kind of like customer segmentation). To start, I need to engineer some features that will segmenting the commentors into clusters:

Numerical features
- Total # of comments by commentor
- Total # of unique articles commented on
- \# of unique articles commented on exactly once
- \# of unique articles commented on more than once
- Duration of commentor activity (Last Comment Date - First Comment Days) in Days


- \# of characters in username
- \# of alpha, numeric, and spaces in username
- Mean, median, minimum, and maxmimum comment length (characters and tokenized words)
- Mean, median, minimum, and maxmimum time between article publication and comment
- Max consecutive days of comments
- Max # of comments posted in a single day
- Days of week comments were made on
- Hours of the day comments were made on
- \# of comments "in season" vs "out of season"
- \# of times commentor has "responded" to another commentor





