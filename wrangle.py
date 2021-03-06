# The Office Wrangle.py File

# imports

import pandas as pd

# color function
def set_color(ratings):
    if ratings < 7.4:
        return 'red'
    elif (ratings >= 7.4) & (ratings < 8.2):
        return 'yellow'
    elif (ratings >= 8.2) & (ratings < 9.0):
        return 'lightgreen'
    elif (ratings >= 9.0):
        return 'darkgreen'

# The Office Function
def the_office():
    '''
    Function to read the office series csv file,
    and drop null values in the data,
    rename columns for readability,
    convert column names to lowercase
    and save the new df to a csv file
    '''
    # reading the office series data from a csv file
    df = pd.read_csv('the_office_series.csv')
    # dropping the GuestStars column, too many null values
    df = df.drop(columns='GuestStars')
    # renaming the columns for readability
    df = df.rename(columns={"Unnamed: 0": "Episode", "EpisodeTitle": "Episode_Title"})
    # convert column names to lowercase
    df.columns = [col.lower() for col in df]
    # adding a color column to the df
    df['color'] = df['ratings'].apply(set_color)
    # saving the office data to a csv
    df.to_csv('the_office.csv')
    
    return df

# Guest Office_fuction
def guest_office():
    '''
    Function to create a df where there are guest stars on the episode,
    drop the null values in the data,
    rename columns for readability,
    convert column names to lowercase
    and save the df to a csv file 
    '''
    # reading the office series data from a csv file
    df = pd.read_csv('the_office_series.csv')
    # dropping the null values in the GuestStars column
    df = df[df.GuestStars.notna()]
    # renaming the columns for readability
    df = df.rename(columns={"Unnamed: 0": "Episode", "EpisodeTitle": "Episode_Title", "GuestStars": "Guest_Stars"})
    # convert column names to lowercase
    df.columns = [col.lower() for col in df]
    # adding a color column to the df
    df['color'] = df['ratings'].apply(set_color)
    # saving the office data to a csv
    df.to_csv('the_office_guest.csv')
    
    return df
    
# Number of episodes per season

def season_episodes():
    '''
    function that takes the office df and 
    makes a new df with the season and 
    number of episodes per season
    '''
    # getting the office data
    df = the_office()
    # creating a new df with seasons and episodes
    df_episodes = df.groupby('season').size().reset_index(name='episodes')
    
    return df_episodes

def max_views():
    '''
    function that takes the office data
    and findes the episode with the most views
    '''
    # getting the office data
    df = the_office()
    # getting the episode data with the most views
    max_views = df.loc[df.viewership.idxmax()]
    
    return max_views

def cluster_df():
    '''
    function to make a dataframe for clustering
    takes the office data and drops columns
    then changes the dataframe to integers
    '''
    # getting the office data
    df = the_office()
    # dropping columns that are not needed for clustering
    df.drop(columns=['episode_title', 'about', 'date', 'director', 'writers', 'color', 'votes', 'duration', 'viewership', 'season'], inplace=True)
    # changing the dataframe type to integers
    #df = df.astype(int)
    
    return df

# time series function

def office_time():
    '''
    fucntion to take the office data and convert the date column
    to datetime, then add year, month, day, weekday columns
    set a new index to the date column, save a csv file and 
    print the date range and shape of df
    '''
    # getting the office data
    df = the_office()
    # converting the date column to datetime
    df.date = pd.to_datetime(df.date)
    # adding columns for year, month, day, and weekday
    df['year'] = df.date.dt.year
    df['month'] = df.date.dt.month
    df['day'] = df.date.dt.day
    df['weekday'] = df.date.dt.day_name()
    # setting the df index to the date column
    df = df.set_index('date').sort_index()
    # saving the office data to a csv
    df.to_csv('office_time.csv')
    # printing out the date range and shape of the df
    print('Date Range:', df.index.min(), 'to', df.index.max())
    print('Shape:', df.shape)
    
    return df

# making a function
def office_time_model():
    '''
    this function takes the office time data and then 
    drops columns not needed for modeling and
    returns a model new df
    '''
    df = office_time()
    
    # dropping columns that are not needed for modeling purposes
    df = df.drop(columns= {'episode_title', 'episode', 'season', 'about', 'director', 'writers', 
                           'color', 'year', 'month', 'day', 'weekday', 'votes', 'duration'})
    print('Model DF Shape:', df.shape)
    
    return df