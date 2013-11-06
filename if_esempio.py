n = int(input("Enter an integer: "))
m = int(input("Enter another integer: "))

while (n+m)%2 == 0:
	print("That's no good. Try again.")
	n = int(input("Enter an integer: "))
	m = int(input("Enter another integer: "))

print("You have entered an even and an odd number")
