from aoutils import Grid


grid = Grid()

with open("grid.txt", "r") as file:
    for line in file:
        grid.add_row(line.strip())
    
grid.set_oob_symbol(".")


sum_pickable = 0

for pos in grid:
    around_positions = list(grid.get_around_map(pos.coords).values())
    around_values = [pos.symbol for pos in around_positions]
    num_frees = around_values.count(".")
    if pos.symbol == "@" and num_frees >= 5:
        sum_pickable += 1

print(sum_pickable)
