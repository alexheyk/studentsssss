# this program will to calculate the student's progress in this class
# units total = 6
# assignments in unit = 5
# total assignments = 30
# assignments done in unit1 = 6
# assignments done in unit2 = 5
# assignments done in unit3 = 6
# assignments done in unit4 = 4
# assignments done in unit5 = 2
# assignments done in unit6 = 0 

a = int(input("How many assignments done in unit 1:"))
b = int(input("How many assignments done in unit 2:"))
c = int(input("How many assignments done in unit 3:"))
d = int(input("How many assignments done in unit 4:"))
e = int(input("How many assignments done in unit 5:"))
f = int(input("How many assignments done in unit 6:"))
g = int(input("How many days student is in the school:"))
progressUnits = ((a + b + c + d + e +f) / 30) * 100 
progressDays = (30/g) * 100
progressTotal = ((int(progressUnits) + int(progressDays)) / 2)
print(str(progressTotal) + " " + "%")






