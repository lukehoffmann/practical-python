bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
# target_height = int(input('How high?')) # 442 # Meters
target_height = 442 # Meters
num_bills = 1
day = 1

while (stack_height := num_bills * bill_thickness) < target_height:
    print(day, num_bills, stack_height)
    day += 1
    num_bills *= 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', stack_height)