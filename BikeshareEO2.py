import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print("Hello! Let\'s explore some US bikeshare data!")


    city = input("Please enter a city(Chicago, New York City or Washington)\n").lower()
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        print("\nInvalid Input!\n")
        city = input("Please enter a city(Chicago, New York City or Washington)\n").lower()


# get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("\nPlease enter the month you will like to analyze\nEnter either January, February, March, April, May, June or all\n").lower()
    while month not in months:
        print("\nInvalid Input!,No such data.\n")
        month = input("\nPlease enter the month you will like to analyze\nEnter either January, February, March, April, May, June or all\n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = input("\nPlease enter the day you will like to analyze\nEnter either Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all\n").lower()
    while day not in days:
        print("\nInvalid Input!,No such data.\n")
        day = input("\nPlease enter the day you will like to analyze\nEnter either Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all\n").lower()


    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Load data file into DataFrame
    data = pd.read_csv(CITY_DATA[city])
    
    # Convert Start Time to datetime format, extract day of week and hour from from Start Time, for popular travel times
    data['month']= pd.to_datetime(data["Start Time"]).dt.month
    data['day of week']= pd.to_datetime(data["Start Time"]).dt.day_name()
    data['hour']= pd.to_datetime(data["Start Time"]).dt.hour
    
    
    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        data = data[data['month'] == month]


    # Filter data by day of week if applicable
    if day != 'all':

        # Filter by day of week to create the new dataframe
        data = data[data['day of week'] == day.title()]

    return data



def time_stats(data):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = data['month'].mode()[0]
    most_common_month = calendar.month_name[most_common_month]
    print('The most common month of travel is:\n',most_common_month)
    
    # display the most common day of week
    most_common_day = data['day of week'].mode()[0]
    print('The most common travel day of the week is:\n',most_common_day)


    # display the most common start hour
    most_common_hour = data['hour'].mode()[0]
    print('The most common hour of travel is:\n',most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(data):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = data['Start Station'].mode()[0]
    print('\nThe most commonly used start station is:\n',most_common_start_station)


    # display most commonly used end station
    most_common_end_station = data['End Station'].mode()[0]
    print('\nThe most commonly used end station is:\n', most_common_end_station)


    # display most frequent combination of start station and end station trip
    most_common_trip_startend = data.groupby(['Start Station'])['End Station'].value_counts().index[0]
    print('\nThe most frequent combination of Start Station and End Station is:\n',most_common_trip_startend)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(data):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = data['Trip Duration'].sum()

    #solving for the total no of days using quotients and remainders

    #solving for the total no of days using quotients and remainders
    #24 * 60 * 60 = 86400 (no of hours in a day * no of mins in 1 hour * no of secs in 1 minute)

    total_days = total_travel_time // (86400)
    total_hrs = total_travel_time % (86400) // (3600)
    total_mins = total_travel_time % (86400) % (3600) // 60
    total_secs = total_travel_time % (86400) % (3600) % 60
    print('The total travel time is {} days, {} hours, {} minutes and {} seconds'.format(total_days, total_hrs, total_mins, total_secs))
    
    
    # display mean travel time
    mean_travel_time = data['Trip Duration'].mean()

    #solving for the mean no of days using quotients and remainders
    #24 * 60 * 60 = 86400 (no of hours in a day * no of mins in 1 hour * no of secs in 1 minute)

    mean_days = mean_travel_time // (86400)
    mean_hrs = mean_travel_time % (86400) // 3600
    mean_mins = mean_travel_time % (86400) % 3600 // 60
    mean_secs = mean_travel_time % (86400) % 3600 % 60
    print('The mean travel time is {} days, {} hours, {} minutes and {} seconds'.format(mean_days, mean_hrs, mean_mins, mean_secs))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(data):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = data['User Type'].value_counts()
    print('The user types breakdown count is:\n',user_types)


    # Display counts of gender
    if 'Gender' in data.columns:
        gender = data['Gender'].value_counts()
        print('\nThe gender breakdown count is:\n',gender)
    else:
        print('\nNo gender information present')


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in data.columns:
        earliest_birth_year = round(data['Birth Year'].min())
        print('\nThe earliest birth year is:', earliest_birth_year)
        most_recent_birth_year = round(data['Birth Year'].max())
        print('\nThe most recent birth year is:', most_recent_birth_year)
        most_common_birth_year = round(data['Birth Year'].mode()[0])
        print('\nThe most common birth year is:', most_common_birth_year)
    else:
        print('\nNo birth year information present')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(data):
    """ Prompt users to see if they want to see 5 lines of raw data, the prompt continues until user enters 'no', or no more raw data """

    raw_data = input("Would you like to see 5 lines of raw data? Enter yes or no.\n")
    if raw_data.lower() == 'yes':
        i = 0
        while True:
            print(data.iloc[i: i+5])
            i += 5
            next_data = input("Do you want to keep viewing the next 5 lines? Enter yes or no.\n")
            if next_data != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        data = load_data(city, month, day)

        time_stats(data)
        station_stats(data)
        trip_duration_stats(data)
        user_stats(data)
        display_raw_data(data)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()


