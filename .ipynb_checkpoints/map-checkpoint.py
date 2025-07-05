import numpy as np

from config import MAP_HEIGHT,MAP_WIDTH 

def create_empty_map():
    return np.zeros((MAP_HEIGHT, MAP_WIDTH), dtype=np.uint8)

def make_walls(map_array):
    
    # Create walls around the 2D map 
    map_array[0, :] = 1  # Top wall
    map_array[-1, :] = 1 # Bottom wall
    map_array[:, 0] = 1 # Left wally
    map_array[:, -1] = 1 # Right wall
       

def make_obstacles(map_array):
    # vertical block
    map_array[100:105, 50:450] = 1

    # 2. Vertical wall
    map_array[50:450, 250:255] = 1

    # 3. Square block
    map_array[150:200, 300:350] = 1

    # 4. L-shaped block
    map_array[300:350, 100:105] = 1
    map_array[345:350, 100:150] = 1

    # 5. T-shaped structure
    map_array[200:205, 400:460] = 1
    map_array[200:260, 428:432] = 1

    # 6. U-shaped obstacle
    map_array[380:430, 300:305] = 1
    map_array[380:385, 300:350] = 1
    map_array[380:430, 345:350] = 1

    # 7. Plus (+) shaped block
    map_array[100:160, 100:105] = 1
    map_array[125:130, 80:130] = 1

    # 8. Letter H block
    map_array[400:430, 100:105] = 1
    map_array[400:430, 130:135] = 1
    map_array[412:418, 105:130] = 1

    # 9. Maze-like corridor
    map_array[50:55, 50:300] = 1
    map_array[55:200, 295:300] = 1
    map_array[195:200, 100:300] = 1
    map_array[100:200, 100:105] = 1

    # 10. Big central block (to dodge)
    map_array[220:280, 220:280] = 1  
    
def create_world():
    world = create_empty_map()
    make_walls(world)
    make_obstacles(world)
    return world     