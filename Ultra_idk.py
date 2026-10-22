def getSum(limit):
    t_sum = 0
    for i in range(1, limit + 1):
        t_sum += i
    return t_sum

while True:
    user_input = input("Hi there! Please enter your age: ")
    if user_input.isdigit() and int(user_input) > 0:
        n = int(user_input)
        break
    else:
        print("Please enter a positive whole number greater than 0.")
expected_sum = (n * (n + 1)) // 2
print(f"Expected sum is {expected_sum}")
loop_sum = getSum(n)
print(f"After calling the function getSum, the sum of all numbers from 1 to {n} is: {loop_sum}")
if loop_sum == expected_sum:
    print("Output verified.")
else:
    print("Output not verified.")



    
    
