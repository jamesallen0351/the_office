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