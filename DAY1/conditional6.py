char = ord(input("Enter any character: "))
#ord() function is used to get the ASCII value of the character

if char>= 65 and char <=91:
    print("It's an uppercase letter.")
elif char >= 97 and char <= 122:
    print("It's a lowercase letter.")
elif char >= 48 and char <= 57:
    print("It's a digit.")
else:
    print("It's a special character.")