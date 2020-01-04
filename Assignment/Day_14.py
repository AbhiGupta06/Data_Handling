"""
Data wrangling using Pandas - Part 2
"""

"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""



"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Titanic
  Filename: 
      titanic.py
  Dataset:
      training_titanic.csv
  Data Description:      
      survival: Survival (0 = No; 1 = Yes)
      pclass: Passenger Class (1 = Upper; 2 = Middle; 3 = Lower)
      name: Name
      sex: Sex
      age: Age 
      sibsp: Number of Siblings/Spouses Aboard
      parch: Number of Parents/Children Aboard
      ticket: Ticket Number
      fare: Passenger Fare
      cabin: Cabin
      embarked: Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

  Problem Statement:
      Titanic ship that crashed in April, 1912.
      Real-world data containing the details of titanic ships passengers list.
      There were lifeboats for only 1178 people
      There were 2224 passengers on board
      Answer the Following:
      0. Total number of Passengers in the dataset
      0. Find all large families (Sibsp > 3)
      0. Find all the features which has missing
      0. Drop the column which has the max missing
      0. Embarked Feature missing values needs to be fixed
      0. Age missing value needs to be fixed
      1. How many people survived the disaster ?
      2. How many people died the disaster ?
      3. Plot the people who survived Vs died appropriately.
      4. Calculate and print the survival rates as proportions (percentage) 
      5. Which gender have greater survival rate ?
         Were females given high priority while rescue.
         Males that survived vs males that passed away
         Females that survived vs Females that passed away
         Also plot it
      6. Does age play a role for survival?
         Since it's probable that children were saved first.
  
  Advanced Problem Statements:
     7. Does Pclass feature plays role in survival
         Survived Vs Died according to Pclass and sex
         Plot it (FactorPlot and CrossTab)
      8. Who was the oldest person survived 
      9. Yougest person survived
      10. Is there a relationship between Pclass and the survival 
          Draw violen plots PClass and Age Vs Survived 
          Sex and Age Vs Survived 
      11. Find the title from the name and show its value counts
          train['title'] = train.Name.str.extract('\, ([A-Z][^ ]*\.)',expand=False)
      12. If a passanger is alone in ship with no siblings, survival rate is 
          If I have a family onboard, I will save them instead of saving myself.
          But there’s something wrong, the survival rate for families 
          with 5–8 members is 0%. Is this because of PClass? Yes this is PClass,
          large families in Pclass3(>3) died.
      13. Everything except ‘PassengerId’, ‘Ticket’ and ‘Name’ would be 
          correlated with a high survival rate
      14. Do Not Delete the Cabin Column, but recreate using Deck
      
      
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
 
     You can test this by creating a new column with a Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.

      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
      
"""

"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
"""

"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""



"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/
    
"""



"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 

"""

"""
Code Challenge
  Name: 
    IGN Analysis
  Filename: 
    ign.py
  Problem Statement:
    Read the ign.csv file and perform the following task :
   
   Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
   
   
   
  Hint:

    The columns contain information about that game:

    score_phrase — how IGN described the game in one word. 
                   This is linked to the score it received.
    title — the name of the game.
    url — the URL where you can see the full review.
    platform — the platform the game was reviewed on (PC, PS4, etc).
    score — the score for the game, from 1.0 to 10.0.
    genre — the genre of the game.
    editors_choice — N if the game wasn't an editor's choice, Y if it was. This is tied to score.
    release_year — the year the game was released.
    release_month — the month the game was released.
    release_day — the day the game was released.



xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
filtered_reviews.head()
      
%matplotlib inline
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

filtered_reviews["score"].hist()
        
"""



"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
"""







