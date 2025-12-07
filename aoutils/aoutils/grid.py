__all__ = ["Grid", "ValueGrid", "get_grid", "get_value_grid"]

class Position:
    def __init__(self, grid, coords, symbol):
        self.__grid = grid
        self.x, self.y = coords
        self.coords = coords
        self.symbol = symbol
    
    @property
    def left(self):
        return self.__grid[self.x - 1, self.y]

    @property
    def right(self):
        return self.__grid[self.x + 1, self.y]

    @property
    def up(self):
        return self.__grid[self.x, self.y - 1]

    @property
    def down(self):
        return self.__grid[self.x, self.y + 1]
    
class ValuePosition(Position):
    def __init__(self, grid, coords, symbol):
        super.__init__()
        self.value = None


class Grid:
    def __init__(self):
        self.__position_type = Position
        self.rows = []
        self.dim_x = None
        self.dim_y = 0
        self.oob_symbol = "X"

    def add_row(self, row):
        if self.dim_x is None:
            self.dim_x = len(row)
        if len(row) != self.dim_x:
            raise ValueError("Wrong row length")
        row = [self.__position_type(self, (i, self.dim_y), sym) for i, sym in enumerate(list(row))]
        self.rows.append(row)
        self.dim_y += 1
    
    def set_oob_symbol(self, symbol):
        self.oob_symbol = symbol

    def __getitem__(self, index):
        x, y = index
        if x < 0 or x >= self.dim_x or y < 0 or y >= self.dim_y:
            return self.__position_type(self, (x, y), self.oob_symbol)
        return self.rows[y][x]
    
    def get_row(self, y):
        return [self[x, y] for x in range(0, self.dim_x)]
    
    def get_columnn(self, x):
        return [self[x, y] for y in range(0, self.dim_y)]
    
    def __setitem__(self, index, new_pos):
        x, y = index
        if x < 0 or x >= self.dim_x or y < 0 or y >= self.dim_y:
            raise IndexError
        self.rows[y][x].symbol = new_pos
    
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
    
    def find_symbol(self, symbol):
        for pos in self:
            if pos.symbol == symbol:
                return pos
            
    def __str__(self):
        ret = ""
        for row in self.rows:
            symbols = [pos.symbol for pos in row]
            ret += "".join(symbols) + "\n"
        ret = ret[:-1]
        return ret
    

class GridIterator:
    def __init__(self, grid):
        self.grid = grid
        self.x = 0
        self.y = 0

    def __next__(self):
        if self.y >= self.grid.dim_y:
            raise StopIteration
        
        pos = self.grid[self.x, self.y]

        self.x += 1
        if self.x >= self.grid.dim_x:
            self.x = 0
            self.y += 1
        return pos


def get_grid(filepath):
    grid = Grid()
    with open(filepath, "r") as file:
        for line in file:
            grid.add_row(line.strip())

    return grid

def get_value_grid(filepath, init_value):
    grid = ValueGrid(init_value)
    with open(filepath, "r") as file:
        for line in file:
            grid.add_row(line.strip())

    return grid


class ValueGrid(Grid):
    def __init__(self, init_value):
        self.values = []
        self.init_value = init_value
        super().__init__()
        self.__position_type = ValuePosition

    def add_row(self, row):
        super().add_row(row)
        for pos in self.rows[-1]:
            pos.value = self.init_value

    def __str__(self):
        ret = ""
        ret2 = ""
        for row in self.rows:
            symbols = [pos.symbol for pos in row]
            values = [pos.value for pos in row]
            ret += "".join(symbols) + "\n"
            ret2 += "".join(str(values)) + "\n"
        ret = ret + "\n" + ret2[:-1]
        return ret