
"""
start
get the numbers of sheets
sheets / 5
round answer to next number
output the results to the user
end
"""

# sheet = 16
# answer = sheet / 5
# rounded = round(answer, 1)
# print("sheet is : ", sheet)
# print("the answer is: ", answer)
# print( "rounded is: ", rounded)

import math

# Input: sheet 
def calculate(sheet):
    # Step 1 
    answer = sheet / 5
    # Step 2
    rounded = math.ceil(answer)
    print("sheet is : ", sheet)
    print("the answer is: ", answer)
    print("rounded is: ", rounded)
    print("=================================")
    # Output: number of stamps needed
    return rounded


output = calculate(16)

# calculate(12000)
# calculate(1000)
# calculate(12000)
# calculate(500)

print("The nummber of stamps needed is: ", output)

#answer = round(sheet / 5)
