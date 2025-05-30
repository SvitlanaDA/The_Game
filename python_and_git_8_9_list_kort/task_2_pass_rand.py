import random
import string

# a, b, c, d, ... z
lower_case = list(string.ascii_lowercase)
# A, B, C, ... Z
upper_case = list(string.ascii_uppercase)
# 0, 1, 2, 3, ... 9
digits = list(string.digits)
# list
my_pass = lower_case + upper_case + digits
# generation password for 8 strings
pass_rand = ''.join(random.choices(my_pass, k=8))

print(f"Generated password: {pass_rand}")