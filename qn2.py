full_name = input("Enter your full name: ")
names = full_name.split()
initials = names[0][0].upper() + "." + names[-1][0].upper()
print(f"Your initials are: {initials}")