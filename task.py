import csv

file_path = 'data.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

data = csv.DictReader(lines)

red_count = 0
yellow_count = 0
green_count = 0

red_time = 0
yellow_time = 0
green_time = 0

green_times = [] 
current_cycle = []
mistake_lines = 0

target_cycle = ['R', 'Y', 'G', 'Y', 'R']
cycle_count = 0
window_size = len(target_cycle)

for row in data:
    red = int(row['Red'])
    yellow = int(row['Yellow'])
    green = int(row['Green'])
    time_active = int(row['TimeActive'])
    time = row['Time']
    
    #occurrences and active times
    if red == 1:
        red_count += 1
        red_time += time_active
    if yellow == 1:
        yellow_count += 1
        yellow_time += time_active
    if green == 1:
        green_count += 1
        green_time += time_active
        green_times.append(time)
        
    #mistakes check
    if red + yellow + green != 1:
        mistake_lines += 1
        
    #creating the current cycle list 
    if red == 1:
        current_cycle.append('R')
    elif yellow == 1:
        current_cycle.append('Y')
    elif green == 1:
        current_cycle.append('G')    
        

for i in range(len(current_cycle) - window_size + 1):
    window = current_cycle[i:i + window_size]
    
    #checking if the window matches the target cycle
    if window == target_cycle:
        cycle_count += 1

#results 
print(f"Red count: {red_count}, Yellow count: {yellow_count}, Green count: {green_count}")
print(f"Red active time: {red_time} seconds, Yellow active time: {yellow_time} seconds, Green active time: {green_time} seconds")
print(f"Green active times: {green_times}")
print(f"Mistake lines: {mistake_lines}") 
print("Number of full cycle occurrences:", cycle_count)