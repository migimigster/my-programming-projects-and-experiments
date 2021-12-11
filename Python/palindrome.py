x=input("Enter word: ")
x=x.lower()
x=x.replace(" ", "")
if x == x[::-1]:
    print("Yes that is a palindrome")
else:
    print("No that is not a palindrome")
    print(x[::-1])
