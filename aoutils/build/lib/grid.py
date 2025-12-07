class Grid:
    def __init__(self):
        self.rows = []
        self.dim_x = None
        self.dim_y = 0
        self.oob_symbol = "X"

    def add_row(self, row):
        if self.dim_x is None:
            self.dim_x = len(row)
        if len(row) != self.dim_x:
            raise ValueError("Wrong row length")
        self.rows.append(list(row))
        self.dim_y += 1
    
    def set_oob_symbol(self, symbol):
        self.oob_symbol = symbol

    def __getitem__(self, index):
        x, y = index
        if x < 0 or x >= self.dim_x or y < 0 or y >= self.dim_y:
            return self.oob_symbol
        return self.rows[y][x]
    
    def __setitem__(self, index, value):
        x, y = index
        if x < 0 or x >= self.dim_x or y < 0 or y >= self.dim_y:
            raise IndexError
        self.rows[y][x] = value
    
    def __iter__(self):
        return GridIterator(self)

    def get_around_map(self, index):
        x, y = index
        around_map = {}
        around_map["top-left"] = self[x-1, y-1]
        around_map["top"] = self[x, y-1]
        around_map["top-right"] = self[x+1, y-1]
        around_map["left"] = self[x-1, y]
        around_map["right"] = self[x+1, y]
        around_map["bot-left"] = self[x-1, y+1]
        around_map["bot"] = self[x, y+1]
        around_map["bot-right"] = self[x+1, y+1]
        return around_map
    

class GridIterator:
    def __init__(self, grid):
        self.grid = grid
        self.x = 0
        self.y = 0

    def __next__(self):
        if self.y >= self.grid.dim_y:
            raise StopIteration
        
        value = self.grid[self.x, self.y]
        ret_x = self.x
        ret_y = self.y

        self.x += 1
        if self.x >= self.grid.dim_x:
            self.x = 0
            self.y += 1
        return (ret_x, ret_y), value
