#Advent of code: day 1
import math

#PART 1
f = open("day_1.txt", "r")
module_weights = f.read().strip().split('\n')

def fuel_required(mass):
    return math.floor(mass/3) -2
        
print(sum([fuel_required(int(x)) for x in module_weights]))

#PART 2
def fuel_required_extra(mass):
    fuel_req = math.floor(mass/3) -2
    if fuel_req <= 0: 
        return 0
    return fuel_req + fuel_required_extra(fuel_req)

print(sum([fuel_required_extra(int(x)) for x in module_weights]))