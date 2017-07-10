from psychopy import gui
import random



## PY0766 Practical Research Skills and Techniques ##
## Kris McCarty ##
## February 2017 ##

## Session 6 ##

##---------------------------------------##
## Part 1 - Your First Program ##
##---------------------------------------##

# 1.1 Below this line, type print "Hello World"


##---------------------------------------##
##Part 2 - Data Types: Strings ##
##---------------------------------------##

quote = "The Knights that say Nee"

# 2.1 Below this line, slice the word 'Knights' out of the variable quote and into the variable called name


# 2.2 Below this line, use reverse slicing to select the word Nee save it in the variable rev


# 2.3 Below this line, save the entire quote in upper case in a variable called emphasis


# 2.4 Below this line, alter the the code to include the newly emphasised quote 

interviewQuote = "I laughed so much when we encountered"


# 2.5 Below this line reproduce the following using the special characters 
#     and string comprehension - you will produce a string then print it
#     save it in the variable scientists 

# First Name: Charles <TAB> Surname: Darwin <TAB> DOB: 12/02/1809
# First Name: Ronald  <TAB> Surname: Fisher <TAB> DOB: 17/02/1890

first = 'Charles'
sur = 'Darwin'
DOB = '12/02/1809'

first2 = 'Ronald'
sur2 = 'Fisher'
DOB2 = '17/02/1890'


 ##---------------------------------------------------##
 ## Part 3 - Data Types: Integers / Floats ##
##---------------------------------------------------##

# 3.1 Change the expression of the sum below (which currently equal 38) to solve 34

b = 12 + 5 * 6 - 4 

#3.2 Alter the mathematical expression below to display the decimal places 

z = 3.0 + 5.0 / 5 ** 6

# 3.3 Find the remainder of mySum below

mySum = 5 % 2

# 3.4 What would we expect out of this equation?

expo = 5 * (3 + 5) ** 2 ** 4

# 1.4073749L

 ##----------------------------------------------------------##
 ## Part 4 - Data Types: Boolean Expressions ##
##---------------------------------------------------------##

# you can try these along with the class

a = 6

b = 7

c = 42


 ##------------------------------------------------------##
 ## Part 5 - Data Types: Containers - Lists  ##
##------------------------------------------------------##

# Lists

# 5.1 Create a list called shopping list below with 5 items in it


# 5.2 Create a variable firstItem that takes the first item from that list


# 5.3 Whats the length of your original list?


# 5.4 Add a further two items to that list


# 5.5 pop the last index off that list and assign it to the variable lastItem



 ##---------------------------------------------------------------##
 ## Part 6 - Data Types: Containers - Dictionaries  ##
##---------------------------------------------------------------##

# 6.1 Create a dictionary called P_info and in it store p_numb, age, occupation and a 
#     boolean of whether they are right handed - make these details up


# 6.2 Call the value of their age in a variable called age below


# 6.3 Add a key to the dictionary called sex and add the value female


 ##----------------------------##
 ## Part 7 - Methods: if  ##
##----------------------------##

# 7.1 write an if statement that decides whether a number (in the variable numberTest) 
#     is even or odd and simply prints 'odd' or 'even'

numberTest = 55


# 7.2 Using the list below, create an if statement which compares whether a name that you input (that saves to variable nameTest)
#     (i have added the syntax for this under PsychoPys DLG Box, simply uncomment it) is in the names list
#     if it is, print "present", if not, print, 'Not on list'


names = ['Jack Beal','Lewis Clark','Ashleigh Cooke','Vicki Costigan','Kyle Gilloway','Chloe Hill',
		 'Mitchell Hogg','Scott Houghton','Connor Leslie','Katie Linden','Lisa McDonald','Dale Metcalfe',
		 'Mikkala Parkhurst'' Bethan Senior','Ellen Smith','George Sweeten','Sarah Whitehouse',
		 'Jonathan Winter', 'Amy Newman']

# info = {}
# info['name'] = ''
# dlg = gui.DlgFromDict(info)
# nameTest = info['name']

##-----------------------##
## Part 8 - Methods: for ##
##-----------------------##

# 8.1 using the if statement you created in 7.1, wrap a for loop around it to 
#     iterate over numberList (predefined) this time please print the number as 
#     well as the diagnosis e.g. "14, is an Even number"
#     use the special string character %i for the job

numberList = (random.randint(0, 10000) for x in range(50000))


# 8.2 add in an additonal condition above that breaks the loop using the keyword break 
#     if it encounters the number 9000 


 ##---------------------------------------------------------------##
 ## Part 9 - While  ##
##---------------------------------------------------------------##

# 9.1 Loop over the below counter using a while loop and print the following statments based on its count
#     be sure to take 5 off the count every time the loop runs. you can do this using whileCounter -= 5
#     while the count is > 300 print 'Huge number'
#     while the count is < 300 but more than 200 print 'getting smaller'
#     while the count is <2000but more than 100 print 'This is tiresome'
#     when the count reaches < 999 print 'bored now' and break the loop with a break statment
#     Note: knowing the condition to put the while argument in may be tricky - how can you ensure it runs until the last elif?

whileCounter = 500


 ##---------------------------------------------------------------##
 ## Part 10 - Functions  ##
##---------------------------------------------------------------##

# 10.1 Create a function that generates participant codes based on the following user input
#     first 2 letters of your mothers maiden name, 2 digit day of your birth, and
#     the first 2 letters of your first name
#     e.g. BA31KR



# 10.2 call that function on the following data and save to a variable pCode
# print the code

MMM = 'Smith'
nom = 'Steve Harris'
dateOfBirth = '12/03/1956'

# 10.3 alter the function so all letters in the code become upper case


 ##---------------------------------------------------------------##
 ## Part 11 - APIs  ##
##---------------------------------------------------------------##

# 11.1 search the matplotlib.pyplot documentation to plot the following data
# Dont forget to import the relevant module! 

year = [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 
        1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 
        1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 
        1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 
        1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 
        1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 
        2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 
        2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 
        2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 
        2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039,
        2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 
        2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 
        2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 
        2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 
        2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 
        2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 
        2094, 2095, 2096, 2097, 2098, 2099, 2100]

pop = [2.53, 2.57, 2.62, 2.67, 2.71, 2.76, 2.81, 2.86, 2.92, 
       2.97, 3.03, 3.08, 3.14, 3.2, 3.26, 3.33, 3.4, 3.47, 
       3.54, 3.62, 3.69, 3.77, 3.84, 3.92, 4.0, 4.07, 4.15, 
       4.22, 4.3, 4.37, 4.45, 4.53, 4.61, 4.69, 4.78, 4.86, 
       4.95, 5.05, 5.14, 5.23, 5.32, 5.41, 5.49, 5.58, 5.66, 
       5.74, 5.82, 5.9, 5.98, 6.05, 6.13, 6.2, 6.28, 6.36, 
       6.44, 6.51, 6.59, 6.67, 6.75, 6.83, 6.92, 7.0, 7.08, 
       7.16, 7.24, 7.32, 7.4, 7.48, 7.56, 7.64, 7.72, 7.79, 
       7.87, 7.94, 8.01, 8.08, 8.15, 8.22, 8.29, 8.36, 8.42, 
       8.49, 8.56, 8.62, 8.68, 8.74, 8.8, 8.86, 8.92, 8.98, 
       9.04, 9.09, 9.15, 9.2, 9.26, 9.31, 9.36, 9.41, 9.46, 
       9.5, 9.55, 9.6, 9.64, 9.68, 9.73, 9.77, 9.81, 9.85, 
       9.88, 9.92, 9.96, 9.99, 10.03, 10.06, 10.09, 10.13, 
       10.16, 10.19, 10.22, 10.25, 10.28, 10.31, 10.33, 
       10.36, 10.38, 10.41, 10.43, 10.46, 10.48, 10.5, 
       10.52, 10.55, 10.57, 10.59, 10.61, 10.63, 10.65, 
       10.66, 10.68, 10.7, 10.72, 10.73, 10.75, 10.77, 
       10.78, 10.79, 10.81, 10.82, 10.83, 10.84, 10.85]

