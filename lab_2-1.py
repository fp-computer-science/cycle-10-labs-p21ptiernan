# Author PT 12/4/20

def sum_to(value):
    for x in range(int(value) + 1):
        total += x
    return total


num = input(" Enter an integer: ")
print(sum_to(num))
