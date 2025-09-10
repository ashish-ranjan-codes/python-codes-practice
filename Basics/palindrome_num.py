# check if a number is palindrome

num = int(input("Enter a number: "))

rev = 0; n = num

while n > 0:
    rev = (rev*10) + n%10
    n = n // 10

if num == rev:
    print(f"{num} is Palindrome")
else:
    print(f"{num} is not Palindrome")