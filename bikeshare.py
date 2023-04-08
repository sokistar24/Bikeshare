import pandas as pd
import time
# dictionary used to read in the city data for bike share services
CITY_DATA = { 'CH': 'chicago.csv',
              'NY': 'new_york_city.csv',
              'WA': 'washington.csv' }


def to_day_of_week(day):
    """" Agrs:
              (int) day: day of the week in interger form to convert to string
        returns:  day of the week in string format
    """
    dict = {0: 'mon', 1: 'tue', 2: 'wed', 3: 'thu', 4: 'fri', 5: 'sat', 6: 'sun'}
    return dict[day]


def to_month(month):
    """" Agrs:
              (int) month : month  of the year  in interger form to convert to string
        returns month  of the year in string format
    """
    dict = {1: 'january', 2: 'febuary', 3: 'march', 4: 'april', 5: 'may', 6: 'june'}
    return dict[month]


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df.drop('Unnamed: 0', inplace=True, axis=1)
    df['month in num'] = df['Start Time'].dt.month
    df['month'] = df['month in num'].apply(to_month)
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['day'] = df['day_of_week'].apply(to_day_of_week)
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        # months = ['january', 'february', 'march', 'april', 'may', 'june']
        # month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]

    return df
def popular_stations_and_trip(df):
    """
    function to compute the most commonly used start station, end station and trip
    Arg pandas dataframe (df) loads in the city data
    return: popular start station, end station and popular trip
    """
    #popular stations and trips with their corresponding value counts
    df['trip combination']=df['Start Station']+" to "+df['End Station']
    pop_start_station=df['Start Station'].mode()[0]
    #pop_start_station_count=df[df['Start Station']==pop_start_station]['Start Station'].count()
    pop_end_station =df['End Station'].mode()[0]
    #pop_end_station_count=df[df['End Station']==pop_start_station]['End Station'].count()
    trip=df['trip combination'].mode()[0]
    return (pop_start_station,pop_end_station,trip)

def trip_duration(df):
    """
    function to compute the total drip and average trip duration within a city
    Arg pandas dataframe (df) loads in the city data
    return: the mean and average trip duration
    """
    total_travel_time=df['Trip Duration'].sum()
    average_trip_time=df['Trip Duration'].mean()
    # add the max trip duration may be as a question
    return(total_travel_time,average_trip_time)

def user_category(df):
    """
    function to compute the  category of the users
    Arg pandas dataframe (df) loads in the city data
    return: user  category
    """
    user_type=df['User Type'].value_counts()
    return user_type
def gender_category(df):
    """
    function to compute the gender category of the users
    Arg pandas dataframe (df) loads in the city data
    return: gender category
    """
    gender=df['Gender'].value_counts()
    return gender
def birth_details(df):
    """
    function to computes the birt details of users
    Arg pandas dataframe (df) loads in the city data
    return: earliest birth year, most recent birt year and popular birth year
    """
    earliest_birth_year=df['Birth Year'].max()
    recent_birth_year=df['Birth Year'].min()
    most_common_birth_year=df['Birth Year'].mode()[0]
    return (earliest_birth_year,recent_birth_year,most_common_birth_year)


# populat travel times
def popular_hour(df):
    """
    function to comupte the most popular travel hour
    Arg pandas dataframe (df) loads in the city data
    return: most popular travel hour
    """
    popular_hour = df['hour'].mode()[0]
    return popular_hour


def popular_month(df):
    """
    function to compute the most popular travel month
    Arg pandas dataframe (df) loads in the city data
    return: most popular travel month
    """
    popular_month = df['month'].mode()[0]
    return popular_month


def popular_day(df):
    """
    function to compute the most popular travel day of the week
    Arg pandas dataframe (df) loads in the city data
    return: most popular travel day of the week
    """
    popular_day_of_week = df['day'].mode()[0]
    return popular_day_of_week


def get_city():
    """
    function to get the city which the user wants to explore
    Arg str: loads in the city data
    return: city
    """

    while True:
        city_code = input('enter city code:\n : CH for Chicago, NY for New York and WA for Washington : ').upper()
        # NY for new york city: CH for chigaco WA for washinton
        if city_code in ('NY', 'CH', 'WA'):
            break
        else:
            print('wrong entry! city code  must be either CH,NY or WA')
            continue

    return city_code


def month_filter():
    """
    function to search data by month if user request

    return: the month user wants to search by
    """
    while True:
        try:
            month_filter = input('would you like to filter by month?: y/n ').lower()

        except:

            print('not a string')
        else:
            if month_filter in ('y', 'n'):
                if month_filter == 'y':
                    while True:
                        try:
                            month = input('enter month : january, febuary, march, april, may,june :  ').lower()
                        except:
                            print(' was not enter as a string: enter month ')
                        else:
                            if month in ('january', 'february', 'march', 'april', 'may', 'june'):

                                break

                            else:
                                print('check that month is in range of allowable months january to june ')
                                continue

                    return month

                else:
                    month = 'all'
                    return month
            else:
                print('enter y or n : ')
                continue


# function to select day of the week filter
def day_of_week_filter():
    """
    function to search data by day of the week  if user request

    return: the day of the week  user wants to search by
    """
    while True:
        try:
            day_filter = input('would you like to filter by day of the week ?: y/n : ').lower()

        except:

            print('enter either y or n ')
        else:
            if day_filter in ('y', 'n'):
                if day_filter == 'y':
                    while True:
                        try:
                            day = input('enter day of week  : mon, tue, wed, fri, sat, sun :  ').lower()
                        except:
                            print(
                                ' was not entered as a string: enter day of week as three letter format e.g mon for monday')
                        else:
                            if day in ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'):
                                return day
                                break

                            else:
                                print('confirm  that that that of week is valid three letter format e.g mon for monday')
                                continue



                else:
                    day = 'all'
                    return day
            else:
                print('enter y or n : ')
                continue


def display_popular_stations_and_trip_duration(dataframe):
    """
    function to search for popular stations, trip duration and other information
    Args: pandas dataframe- containing city data
    display data based on users request
    """

    while True:

        try:
            search_key = int(input('enter 1: for popular station , 2: for common trip duration, 0 for others  :  '))
        except:
            print('oops not a digit  enter a valid digit between 0,1,2 : ')
            continue
        else:
            if search_key in (1, 2, 0):

                if search_key == 1:

                    start_station, end_station, trip = popular_stations_and_trip(dataframe)
                    print(f'most popular start station is : {start_station}')
                    print(f'most popular end station is :  {end_station}')
                    print(f'most popular strip is from :  {trip}')
                    continue
                elif search_key == 2:
                    total_travel_duration, average_trip_duration = trip_duration(dataframe)
                    print(f'total travel duration for  is : {total_travel_duration} secs ')
                    print(f'the average is :  {average_trip_duration} secs')
                    continue

                elif search_key == 0:
                    break
            else:
                print('number not withing range enter values in 0,1,2')
                continue


# do you want to search for travellers details

# do you want to search for travellers details

def display_users_info(city, df):
    """
    function to search for users based of the  city info such as gender and date of birth

    Args- str (city): city user chooses to explore
          pandas dataframe (df) : dataframe containg city data
    """
    while True:
        if city in ('CH', 'NY'):

            try:
                key_search = int(input('enter 1 for user category 2 for Gender and 3 for date of birth 0 for none :  '))

            except:
                print('not a valid number ! :')

            else:
                if key_search in (0, 1, 2, 3):
                    if key_search == 1:
                        print('users category distribution is : ')
                        user_cat = user_category(df)
                        print(user_cat)
                    elif key_search == 2:
                        print('users gender distribution is : ')
                        gender_cat = gender_category(df)
                        print(gender_cat)
                    elif key_search == 3:
                        print('users birth details : \n ')
                        earliest_birth_year, recent_birth_year, most_common_birth_year = birth_details(df)
                        print(f'earliest birth year is {earliest_birth_year}')
                        print(f'recent birth year is {recent_birth_year}')
                        print(f'most common birth year  is {most_common_birth_year}')
                    elif key_search == 0:
                        break
                else:
                    print('number not within range ')
        if city == 'WA':
            user_cat = user_category(df)
            print(user_cat)
            break


def display_popular_travel_times(day, month, df):
    """
    search popular travel times either: day of week, depending on users request
    Agrs- str (day): day of the week
          str (month): month of the year
          pandas dataframe : (df) dataframe containing city data

    """
    most_common_hour = popular_hour(df)
    print(f' most popular hour is : {most_common_hour}:00 hours')
    if day == 'all' and month == 'all':
        pop_day = popular_day(df)
        pop_month = popular_month(df)

        print(f' most popular day of week  is  : {pop_day}')
        print(f' most popular month is         : {pop_month}')
    if day == 'all' and month != 'all':
        pop_day = popular_day(df)

        print(f' most popular day of week is  : {pop_day}')
    if day != 'all' and month == 'all':
        pop_month = popular_month(df)

        print(f' most popular month is : {pop_month}')


def view_raw_data(df):
    """

     function takes in dataframe and continually returns 5 rows if the user request un until the all data is displayed

     Args: pandas dataframe =df which contains  city data to be viewed

     returns : 5 rows of the city data at each iteration


    """
    view_data = 'y'
    while view_data != 'n':

        view_data = input('do you want to view raw city data? : y/n :').lower()

        if view_data in ('y', 'n'):

            if view_data == 'y':
                start, end = 1, 6

                if end > len(df):
                    end = len(df)
                    print(df.iloc[start:end])
                else:
                    print(df.iloc[start:end])

                while view_data != 'n':

                    view_data = input('to view more data press y to continue n end to stop: y/n :')
                    if view_data in ('y', 'n'):

                        if view_data == 'y':
                            start = end
                            end = start + 5
                            if end > len(df):
                                end = len(df)
                                view_data = 'n'
                                print(df.iloc[start:end])
                                print('you have viewed all the city data thank you !  ')
                            else:
                                print(df.iloc[start:end])

                        else:
                            print('proceed to view other content: ')

                    else:
                        print('wrong input enter y/n : ')
            else:
                print('proceed to view other content : ')
                break
        else:

            print('wrong input enter y/n : ')


def end_or_continue():
    """
    prompts if the user wants to continue exploring other cities or stop

    return: either the search should continue or end
    """
    while True:
        try:
            search_on = input('enter : y to explore other cities n to stop : ').lower()

        except:

            print('string was not entered')
            continue
        else:
            if search_on in ('n', 'y'):

                if search_on == 'n':
                    print('thanks for visiting bike share services')
                    return search_on
                else:
                    print('which city would you like to explore next: ')
                    return search_on
            else:
                print('wrong entry enter either y or n : ')
                continue


search_on = 'y'
print('welcome to bikeshare services')
while search_on == 'y':
    # search for city to explore

    city = get_city()

    # applying month filter

    month = month_filter()

    # applying day of week filter

    day = day_of_week_filter()
    print('city data loading ... : ')
    start_time = time.time()
    # calling the load function to load the city data based on day and month filter applied
    df = load_data(city, month, day)

    loading_time = round((time.time() - start_time), 2)

    print(f'data took : {loading_time} secs to load ')
    view_raw_data(df)
    # searh popular stations or trips or others
    print('search popular stations, trips and others : \n')

    display_popular_stations_and_trip_duration(df)
    # search popular travel details
    print(f' search users details : in {city}  ')

    display_users_info(city, df)

    # would you like to search popular travel times
    print('most popular travel times are : ')
    display_popular_travel_times(day, month, df)

    search_on = end_or_continue()