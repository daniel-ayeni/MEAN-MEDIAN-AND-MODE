'''
'import' ceil for use in the 'median' method
'''


from math import ceil


'''
# inputted_value = Values inputted from the user.
# total_inputted_value = Counting the number of values inputted by the user.
'''


inputted_value = input("Enter values: ")
total_inputted_value = len(inputted_value)


''' 
# 'mean' method created to calculate average from the sum of the values from the user.
# Formula for average is the sum_of_inputted_value divided by the total_inputted_value.
# 'for' statement is used to get the sum_of_inputted_values that is first initialized to zero.
#  'index' is incremented to get each 'value' from the 'inputted_value'.
'''


def mean():
    sum_of_inputted_values = 0
    index = 0
    for values in range(total_inputted_value):
        value = inputted_value[index]
        sum_of_inputted_values = sum_of_inputted_values + int(value)
        index += 1
    __average = sum_of_inputted_values / total_inputted_value
    print('MEAN: ', str(round(__average, 2)))


''' 
# 'median' method created to find the middle number from the 'total_inputted_value'.
# The first 'if' statement is used to control how many middle numbers are to be displayed. That is, if the 
    'total_inputted_value' is even, the middle number to display will be two.
# Ceil function is used to round 'ceil' to the next whole number. 
'''


def median():
    if total_inputted_value % 2 != 0:
        __middle_number = ceil(total_inputted_value / 2) - 1
        print('MEDIAN:', str(inputted_value[__middle_number]))

    else:
        __middle_number = round(total_inputted_value / 2)
        second_middle_number = __middle_number - 1
        print('MEDIAN: ', str(inputted_value[second_middle_number]), 'and',
              str(inputted_value[__middle_number]))


''' 
# 'mode' method created to find the most occurring number from the 'inputted_value'.
# The first 'for' statement is used to iterate through the 'inputted_value'
# The second 'for' statement is used to iterate through the 'inputted_value' and compare each value to the value from
    the first 'for' statement. 'if' the value is the same as that from the first 'for' statement,
    'increment_for_set_value_occurrence' is increased by one. else, the second 'for' loop continues by increasing
    'index_of_second_range' by one.
# 'if' the 'frequency_of_occurrence' which is first assigned the value of zero is less than 
    'increment_for_set_value_occurrence', 'frequency_of_occurrence' equals to the 'increment_for_set_value_occurrence'
    and the mode_list is cleared to append the higher 'increment_for_set_value_occurrence'.
# 'elif', 'frequency_of_occurrence' equals 'increment_for_set_value_occurrence', 'set_value' added to the 'mode_list'
# 'else', it is ignored and 'frequency_of_occurrence' remains the same
# 'cleared_mode_list' is an attribute created to hold the cleaned value of mode_list (i.e all brackets and quotes have
    been removed)
     
'''


def mode():
    first_range_index = 0
    frequency_of_occurrence = 0
    mode_list = []
    for i in range(total_inputted_value):
        set_value = inputted_value[first_range_index]
        index_of_second_range = 0
        increment_for_set_value_occurrence = 0
        for c in range(total_inputted_value):
            second_range_set_value = inputted_value[index_of_second_range]
            if int(second_range_set_value) == int(set_value):
                increment_for_set_value_occurrence += 1
                index_of_second_range += 1
            else:
                index_of_second_range += 1
        if frequency_of_occurrence < increment_for_set_value_occurrence:
            frequency_of_occurrence = increment_for_set_value_occurrence
            # _mode = set_value
            mode_list.clear()
            mode_list.append(set_value)
        elif frequency_of_occurrence == increment_for_set_value_occurrence:
            mode_list.append(set_value)
        else:
            frequency_of_occurrence = frequency_of_occurrence
        first_range_index += 1
    cleared_mode_list = ", ".join(sorted(set(mode_list)))
    print('MODE: ', cleared_mode_list)
    print('occurred', frequency_of_occurrence, 'times in the set')


'''
# 'statistics' method is defined to call all the methods created at once and print the 'total_inputted_value'.
'''


def statistics():
    mean()
    median()
    mode()
    print('The total number of value inputted is:', str(total_inputted_value))

# 'statistics' method is called here
statistics()
