print()
# Displays all errors in the password
pass_p = str(input("Enter password: "))
if len(pass_p) < 8:
        print("Password is invalid. Reason: Too short.")
if "Python" not in pass_p:
        print ("Password is invalid. Reason: Does not contain 'Python'.")
if " " in pass_p:
            print("Password is invalid. Reason: Contains spaces.")

if len(pass_p) >= 8 and "Python" in pass_p and " " not in pass_p:
    print("Password is valid.")

print("Thanks!")