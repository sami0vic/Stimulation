import math
import time

def calculate_point_positions(num_points, angular_speeds, time):
    
    radius = 1
    center = (0, 0)
    angle_steps = [angular_speed * time for angular_speed in angular_speeds]
    
   
    point_positions = {}
    for i in range(num_points):
        angle = i * angle_steps[i]
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        point_positions[f"Point_{i+1}"] = (x, y)
    
    return point_positions

def sort_points_by_position(point_positions):
   
    sorted_points = sorted(point_positions.items(), key=lambda x: math.atan2(x[1][1], x[1][0]))
    
   
    sorted_point_names = [point[0] for point in sorted_points]
    
    return sorted_point_names


num_points = 3
angular_speeds = [10, 15, 20]  
time_increment = 1  


initial_times = [i / angular_speeds[i] for i in range(num_points)]


previous_permutation = None
consecutive_count = 0

# Loop to display points until a permutation is identified for the second time
for initial_time in initial_times:
    t = initial_time
    while True:
        point_positions = calculate_point_positions(num_points, angular_speeds, t)
        sorted_point_names = sort_points_by_position(point_positions)
        sorted_point_names_str = ' '.join(sorted_point_names)

        # Check if the current permutation is the same as the previous one
        if sorted_point_names_str == previous_permutation:
            consecutive_count += 1
        else:
            consecutive_count = 1  # Reset consecutive count if the permutation changes

        # Check if the current permutation has been seen before
        

        # Print the sorted point names for the current time if it's different from the previous one
        if sorted_point_names_str != previous_permutation:
            print(f"At time {t:.2f}:", sorted_point_names_str)
        
        # Update the previous permutation
        previous_permutation = sorted_point_names_str

        # Increment time
        t += time_increment
        time.sleep(time_increment)
