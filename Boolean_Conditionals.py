#Booleans
#Python has a type of variable called bool. It has two possible values: True and False.
x = True
print(x)
print(type(x))
# R//True

#Rather than putting True or False directly in our code, we usually get boolean values from boolean operators. 
#These are operators that answer yes/no questions. We'll go through some of these operators below.

#Comparison Operations
#Operation	Description		Operation	Description
#a == b	a equal to b		a != b	a not equal to b
#a < b	a less than b		a > b	a greater than b
#a <= b	a less than or equal to b		a >= b	a greater than or equal to b

def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return age >= 35

print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))
#R//Can a 19-year-old run for president? False
#Can a 45-year-old run for president? True

