# The Office Series Data

Repo for exploring The Office data

![the_office](the_office.jpg)

## "I Understand Nothing."  - Michael Scott

## Data Dictionary
| Feature | Definition | Data Type | Notes |
| ------- | ---------- | --------- | ----- |
| episode | number of episode | int64 | index of episode number starting at zero |
| season  | season number | int64 | season number that the episode was in |
| episode_title | title of the episode | object | episode title |
| about | what the episode is about | object | summary of what the episode is about |
| ratings | episode ratings | float64 | viewer ratings for the episode |
| votes | number of votes | int64 | number of votes for ratings in the episode |
| viewership | number of episode views | float64 | how many views there were of the episode in millions |
| duration | how long the episode is | int64 | length of the episode |
| date | day episode aired on tv | object | day the episode first aired on tv (changed to datetime in timeseries) |
| director | who directed the episode | object | specific director for the episode |
| writers | names of writers | object | names of writers who wrote the episode |
| color | color based on ratings | object | color category based on episode ratings (red, yellow, lightgreen, darkgreen) |


# Planning

- Initial Thoughts:
    - The office is one of my favorite TV shows
    - Let's see how popular the office is
    - What is the most popular episode(s) / season(s)
    - How was each episode viewed? How many viewers?
    - Maybe clusters of episodes/season popularity
    - Time series of views or ratings
    - Guest stars popularity / views ?


# Acquire

- Download The Office Series csv file
- Open csv file in a jupyter notebook


# Prepare

- Checked for null values
- Created Guest DF and then dropped GuestStars on original df
- Added color column based off ratings
- Clean up column names for readability
- Save new df to csv file
- Converted date column to timeseries and save new df


# Explore

- Look at episode with the most views
- Look at number of seasons and episodes per season
- Histogram of the data
- Scatterplots and bar charts

# Modeling

- Time Series:
    - Last Observed Value
    - Simple Average
    - Moving Average

- Clustering:
    - K-Means
    - Elbow Method

# Conclusion

#### Most popular episode: "Stress Relief"

- Here is a image from that episode

![stress_relief](dwight.jpeg)


- 9 Total seasons of The Office
- First episode aired on March 24th 2005 (also my birthday)
- The last episode aired on May 16th 2013 (also the highest rated episode of the entire series)


## Source

- The office data set was obtained from: [The Office Data](https://www.kaggle.com/nehaprabhavalkar/the-office-dataset)

- Watch The Office here: [The Office](https://www.peacocktv.com/the-office-on-peacock?gclsrc=aw.ds&gclid=CjwKCAiAlfqOBhAeEiwAYi43FxAbt_tCgVsAz1kXmuvdiZzYmbLT9JaXC0GSKn0SxT6KFDmE5P9WDhoCPb8QAvD_BwE&gclsrc=aw.ds)