'''
This code checks if you are able to run for president. If you are over 35, a US Citizen and have 14 years of residency in the US. 
If you are, it'll output that you are eligible, if not, it'll output that you aren't eligible.
by Ben
'''
age = int(input("Age: "))
citizen = input("Born in the U.S.? (Yes/No): ")
residency = int(input("Years of Residency: "))

if (age >= 35) and (citizen == "Yes") and (residency >= 14):
    print("You are eligible to run for president!")

else:
    print("You are not eligible to run for president.")
