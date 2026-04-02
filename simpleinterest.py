p_amount = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate of interest: "))
time = int(input("Enter the time period: "))

simple_interest = (p_amount*rate*time)/100
print("The simple interest is:",simple_interest)