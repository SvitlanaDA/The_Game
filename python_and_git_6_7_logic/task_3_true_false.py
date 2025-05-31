a = True
b = False
c = True
print((a & b), " - True + False = False")
print((a | b), " - True OR False = True")
print((not b), " - NOT False = True")
print(((a & c) | b), " - (True + True = True), True OR False = True")
print((a & (b | c)), " - (False OR True = True), True + True = True")