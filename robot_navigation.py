import sys
from collections import deque

# Function to parse the grid and locate the starting position and all avocado locations
def parse_input(grid):
    rows = len(grid)
    cols = len(grid[0])
    start = None
    avocados = []

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'x': # If the cell contains the starting position 'x'
                start = (i, j)
            elif grid[i][j] == '@': # If the cell copntains an avocado '@'
                avocados.append((i, j))
    return start, avocados

# Function to perform Breadth-First Search(BFS) to calculate shortest paths from a start point
def bfs(grid, start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Possible movement directions (up, down, left, right)
    queue = deque([start]) # Initialize the queue with start position
    distances = {start: 0} # Distance from start to itself is zero

    # Process each point in the queue
    while queue:
        current = queue.popleft() # Remove and get the current point from the queue
        current_distance = distances[current] # Current distance from start to this point
        
        # Explore each possible direction from the current point
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1]) # Calculate the neighbor's coordinates
            # Check if the neighbor is within grid bounds and not an obstacle
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if grid[neighbor[0]][neighbor[1]] != '#' and neighbor not in distances:
                    distances[neighbor] = current_distance + 1 # Update the distance to this neighbor
                    queue.append(neighbor) # Add the neighbor to the queue for further exploration
    return distances 

def solve_tsp_dp(distances, points):
    n = len(points) # Number of points to visit, including the starting point
    all_sets = 1 << n # Calculate the total number of possible sets (2^n) where each point can be visited or not
    dp = [[float('inf')] * n for _ in range(all_sets)] # Initialize the DP table 
    dp[1][0] = 0  # start from the first point, which is the robot's starting position
    
    # Iterate over each subset of visited nodes represented by 'mask'
    for mask in range(1, all_sets):
        # Iterate over each possible ending point for the subset 'mask'
        for end in range(n):
            if mask & (1 << end):  # if end is included in mask
                prev_mask = mask ^ (1 << end) # Calculate the subset excluding the 'end' point
                for prev in range(n):
                    if prev_mask & (1 << prev):  # if prev is included in prev_mask
                        dp[mask][end] = min(dp[mask][end], dp[prev_mask][prev] + distances[prev][end]) # Update the DP table by considering moving from 'prev' to 'end'

    # Find the minimum cost to visit all points and end at any point
    final_mask = all_sets - 1
    min_cost = min(dp[final_mask][end] for end in range(n))
    
    # Reconstruct the path
    path = []
    last = min(range(n), key=lambda i: dp[final_mask][i])
    mask = final_mask
    
    # Backtrack to reconstruct the path taken to find the minimum cost
    while mask:
        path.append(points[last])
        prev_mask = mask ^ (1 << last)
        prev_last = None
        
        # Find the previous point that leads to the current 'last' point optimally
        for i in range(n):
            if prev_mask & (1 << i) and dp[prev_mask][i] + distances[i][last] == dp[mask][last]:
                prev_last = i
                break
        # Move to the previous point and update the mask
        last = prev_last
        mask = prev_mask
        
    # Return the minimum cost and the path in reverse order (from start to last visited)
    return min_cost, path[::-1]


# Function to read the 2D map from the input file
def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
    return grid

# Function to write the result to the output file
def write_output_to_file(output_path, tsp_solution, path_indices, points):
    with open(output_path, 'w') as file:
        file.write(f"{tsp_solution}\n")
        for index in path_indices[1:]:  # path_indices should contain integers
            # Convert index back to coordinate
            coord = points[index]
            file.write(f'{coord[0]},{coord[1]}\n')


def main(input_file, output_file):
    grid = read_grid_from_file(input_file)
    start, avocados = parse_input(grid)
    if not start:
        print("No starting position found")
        return
    if not avocados:
        print("No avocados found")
        return

    points = [start] + avocados # List of all points to visit (start + avocados)
    point_indices = {point: idx for idx, point in enumerate(points)}
    all_distances = {p: bfs(grid, p) for p in points} # Calculate shortest paths from each point to all others
    distances = [[float('inf')] * len(points) for _ in range(len(points))]

    for i, point1 in enumerate(points):
        for j, point2 in enumerate(points):
            distances[i][j] = all_distances[point1].get(point2, float('inf'))  # Use point1 and point2 to get distance

    tsp_solution, path = solve_tsp_dp(distances, points)
    if tsp_solution == float('inf'):
        print("Complete path to all avocados is not possible due to accessibility issues.")
        return
    else:
        path_indices = [point_indices[p] for p in path]  # List of indices for points in the path
        write_output_to_file(output_file, tsp_solution, path_indices, points)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python robot_navigation.py input_file.txt output_file.txt")
    else:
        input_file, output_file = sys.argv[1], sys.argv[2]
        main(input_file, output_file)

