#Quiz
list1=[None]*10
print(len(list1))
# o/p - 10 [[None] printed 10 times.]
# If we simply print list1, the output will be 10 * None.

# MyList=[10, 20, 30, 40]
# MyList.append(60)
# print(MyList)
# o/p - [10, 20, 30, 40, 60]

#invalid statement 
# list1 = [1, 2, 3] and list2 = [4, 5, 6] are given
# list1*2.5 
#why invalid ? In python repetition should be integral only
#Integral: This means "whole" or referring to integers (numbers without decimals)

# Names = [ 'Bob ' , 'Peter' , 'Jack' , 'Jackson' , 'Harry' ]
# empty_list = Names [-1: -6: 1]
# print(len(Names))
# print(empty_list)
# o/p - []
#  the slicing expression Names[-1: -6: 1] does not reverse the order of the list.
# Names[-1:]: This selects elements starting from the last element (-1 index) to the end of the list. Since the step value is positive (1), it means it's selecting elements in the forward direction.
# Names[-1: -6: 1]: This specifies a step size of 1 and selects elements from the last element (-1 index) to the 6th element from the end (-6 index) in the forward direction.
# Since the start index is after the end index, the resulting slice will be an empty list because the range specified by the indices does not contain any elements. In Python slicing, when the start index is greater than or equal to the end index (and the step size is positive), the result is an empty list. Therefore, Names[-1: -6: 1] will result in an empty list [].

#reversed 
# reversed_check = Names[::-1]
# print(reversed_check)
# o/p - ['Raju', 'Harry', 'Jackson', 'Jack', 'Peter', 'Bob ']


# list =[ 1 , [2,3,] ,4  , 5 , [6,7] ,[ 8 ,9] ,10 ]
# number_ind = list[5]
# print(number_ind)
# o/p - [8,9]

# list=[1,2,3,4,5]
# new_val = list [1:3]
# print(new_val)
# list[1:3] = [7,8,9]
# print(list)
# o/p - [1, 7, 8, 9, 4, 5]
# We are first slicing from index 1 to 3 and then inserting new values i.e, 7,8,9

# list =['python ', 'is', 'a', 'userfriendly', 'programming', 'language']
# new_list = list[0:6:2]
# print(new_list)
# Starting Index is 0 , Ending is 6 , StepSize is 2
