num = int(input("enter a value: "))
rev = 0
temp = num
while temp>0:
    rem = temp % 10
    rev = rev * 10 + rem
    temp =(temp//10)
if rev == num:
    print("this is a palindrome number.")
else:
    print("this is not a palindrome number.")        