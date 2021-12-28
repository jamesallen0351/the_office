# The Office Wrangle.py File

# imports

import pandas as pd

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
    # saving the office data to a csv
    df.to_csv('the_office_guest.csv')
    
    return df
    