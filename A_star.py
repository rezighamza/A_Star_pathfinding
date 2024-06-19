"""
Thanks to Sebastian Lague for the tutorial on A* Pathfinding Algorithm
https://www.youtube.com/watch?v=-L-WgKMFuhE
the original code is in C# and i have converted it to python with some modifications 
because the original code is heavily based on Unity Engine and the implementation with game objects
"""
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to the current node
        self.h = 0  # Heuristic cost from the current node to the end node
        self.f = 0  # Total cost of the node (g + h)

    def __eq__(self, other):
        return self.position == other.position  # Compare nodes based on their position
"""
Manhattan distance heuristic
The Manhattan distance heuristic calculates the distance between two points on a grid based on the sum of the absolute differences of their x and y coordinates.
This heuristic is admissible, meaning it never overestimates the cost to reach the goal node from the current node.
The Manhattan distance is calculated as follows:
distance = abs(x1 - x2) + abs(y1 - y2)
where (x1, y1) is the position of the current node and (x2, y2) is the position of the goal node.
"""
def manhattan_distance(node_position, end_position):
    return abs(node_position[0] - end_position[0]) + abs(node_position[1] - end_position[1])


def astar(grid, start, end):
    open_list = []
    closed_list = []

    start_node = Node(start)
    end_node = Node(end)

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        # Check if the current node is the goal node 
        # if so , return the reversed path 
        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] < 0 or node_position[0] >= len(grid) or node_position[1] < 0 or node_position[1] >= len(grid[0]):
                continue # Ignore nodes outside the grid
            if grid[node_position[0]][node_position[1]] != 0:
                continue # Ignore obstacles
            new_node = Node(node_position, current_node)
            if new_node in closed_list:
                continue # Ignore nodes that have already been evaluated
            children.append(new_node)

        for child in children:
            # Calculate the cost of the child node
            child.g = current_node.g + 1
            child.h = manhattan_distance(child.position, end_node.position)
            child.f = child.g + child.h

            if any(open_node for open_node in open_list if child == open_node and child.g >= open_node.g):
                continue

            open_list.append(child)
            
    # Return None if no path is found
    return None  

def read_grid_from_file(file_path):
    # wrap all this in test to check if the file exists
    try:
        with open(file_path, 'r') as file:
            grid = [list(map(int, line.split())) for line in file]
        return grid
    except FileNotFoundError:
        print("File not found")
        exit(1)


if __name__ == '__main__':
    grid_file = 'grid.in'
    grid = read_grid_from_file(grid_file)
    
    start = (0, 0)
    end = (4, 4)

    path = astar(grid, start, end)
    print("Path:", path)
