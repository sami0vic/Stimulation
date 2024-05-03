import math

def calculate_particle_position(angular_speed, angular_acceleration, time):
    initial_angle = 0
    angle = initial_angle + angular_speed * time + 0.5 * angular_acceleration * time ** 2
    angle %= 2 * math.pi
    return angle

def calculate_all_particle_positions(num_particles, angular_speeds, angular_accelerations, time):
    particle_positions = {}
    for i in range(num_particles):
        position = calculate_particle_position(angular_speeds[i], angular_accelerations[i], time)
        particle_positions[f"Particle_{i+1}"] = position
    sorted_particles = sorted(particle_positions, key=particle_positions.get)
    return sorted_particles

num_particles = 3
angular_speeds = [1, 2, 3]
angular_accelerations = [0.1, 0.2, 0.3]

time_increment = 0.1

total_time = 10
current_time = 0
previous_permutation = None

while current_time <= total_time:
    sorted_particles = calculate_all_particle_positions(num_particles, angular_speeds, angular_accelerations, current_time)
    current_permutation = " ".join(sorted_particles)
    
    if current_permutation != previous_permutation:
        print(current_permutation)
        previous_permutation = current_permutation

    current_time += time_increment
