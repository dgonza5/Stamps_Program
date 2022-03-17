
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

def calculate(sheet):
    answer = sheet / 5
    rounded = round(answer, 1)
    print("sheet is : ", sheet)
    print("the answer is: ", answer)
    print( "rounded is: ", rounded)
    print("=================================")
    return rounded


output = calculate(1000)
# calculate(12000)
# calculate(1000)
# calculate(12000)
# calculate(500)

print("the return statement is: ", output)

#answer = round(sheet / 5)
