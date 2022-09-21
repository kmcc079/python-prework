# QUESTION 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    '''display hello_USERNAME'''
    print("hello_" + input("What is your username? ").upper() + "!")

hello_name('user_name')


# QUESTION 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    '''print all odd numbers from 1-100'''
    for num in range(1, 100, 1):
        if num % 2 != 0:
            print(num) 

first_odds()


# QUESTION 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    '''Return the max number of a given list'''
    print(max(a_list))

list1 = ['42', 'universe', 'answer', 'Deep Thought', '7.5']
list2 = [85, 27, 132, 90, 11]

max_num_in_list(list1)
max_num_in_list(list2)


# QUESTION 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    '''return True if given year is a leap year and False if given year is not'''
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                print("It is a leap year!")
                return True
            else:
                print("It is not a leap year.")
                return False
        else:
            print("It is a leap year!")
            return True
    else:
        print("It is not a leap year.")
        return False

year_1 = 1994
year_2 = 2012

is_leap_year(year_1)
is_leap_year(year_2)


# QUESITON 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    a_list = sorted(a_list)
    if a_list == list(range(a_list[0], a_list[-1] +1)):
        print("True")
        return True
    else:
        print("False")
        return False
        

list1 = [8, 10, 12, 15, 24, 32]
list2 = [-3, -2, -1, 0, 1, 2, 3]
list3 = [1, 3, 2, 5, 4]

is_consecutive(list1)
is_consecutive(list2)
is_consecutive(list3)