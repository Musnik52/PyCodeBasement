num = int(input("insert a double-digit number: "))
print("Both digits are the same!" if num//10 == num%10 and num!=11 else "The digits are not the same, or they're both 1" )