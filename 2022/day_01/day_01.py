max_sum = 0
calorie_list = []

with open("input/input.txt", "r") as file:
    lines = file.readlines()
    current_sum = 0
    for line in lines:
        line = line[:-1]  
        if line != "":
            current_sum += int(line)
        else:
            calorie_list.append(current_sum)
            max_sum = max(max_sum, current_sum)
            current_sum = 0
    calorie_list.append(current_sum)

calorie_list.sort(reverse=True)

print(f"Part 1: {max_sum}")
print(f"Part 2: {sum(calorie_list[:3])}")