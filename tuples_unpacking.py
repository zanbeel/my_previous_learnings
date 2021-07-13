#tuples are immytable meaning that cannot be changed
#tuples use parenthasis like list
#list can be reassigned but tuples cannot be ie

# list=[1,2,3]
# print(list)
#  #to assign a new name in this list 
# list[0]='New'
# print(list)

# type(list)

# t=(1,2,3)
# print(t)
# t=('one', 2,3)
# print(t)
# type(t)

# s='hello'
# print([1])

# stock_prices=[('apple', 200),('google',100),('microsoft',50)]
# for prices in stock_prices: 
#     print(prices)

# we can individually grab those items from tuples
# stock_prices=[('apple', 200),('google',100),('microsoft',50)]
# for ticker,prices in stock_prices:
#     print(prices+(0.1*prices))

# work_hours = [('Abe',100),('Bill',200),('Don',500)]

# def employee_check(work_hours):

#     current_max=0
#     employee_of_the_month=''
# #current_max will start off at zero 
# # and it is going to compare each employees current max hours
# #and employee_of_the_month=''
# #we will keep that empty bcz at the end we need to retrun a tuple
# # it will compare each employees current hours to current max hour 
# # and if they beat the current max hours it will reset the current max
# # to their value and it will reset the employee of the month to new value
# #we will do for loop to see this
#     for employee, hours in work_hours:
# # which we will call in every tuple like 'abe:100' a
# # nd we will check the following
#         if hours>current_max:
#     # i will reset my current max equal to the hours
#             current_max=hours
#     # and then the employee of the month is going to be 
#     # equal to employee of that tuple, which means my first call 
#     # start off at zero so my firt tuple apple:100 will beat that zero 
#     # and abe starts off as employee of the month and current max hours to beat is
#     # 100 hours
#             employee_of_the_month= employee
#         else:
#             pass
#     return(employee_of_the_month,current_max)
# then print your output by printing employee check which is Don and work hours which is 800


work_hours = [('Abe',900),('Bill',700),('Don',800)]

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ' '

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
        
    return (employee_of_month,current_max)

print(employee_check(work_hours))