#Advent of code 2019: Day 4

#PART 1

def check_isvalid(password):
    return list(password) == sorted(password) and max([password.count(digit) for digit in password]) >= 2

print(sum(check_isvalid(str(password)) for password in range(124075, 580769 + 1)))

#PART 2
def check_isvalid_2(password):
    return list(password) == sorted(password) and 2 in [password.count(digit) for digit in password]

print(sum(check_isvalid_2(str(password)) for password in range(124075, 580769 + 1)))