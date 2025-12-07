from aoutils import *

lines_splitted = get_lines_splitted("problems.txt")
print(lines_splitted)



class Equation:
    def __init__(self):
        self.values = []
        self.operator = "+"

    def add_value(self, value):
        self.values.append(value)
    
    def set_operator(self, operator):
        self.operator = operator

    def calculate(self):
        if self.operator == "+":
            return self.add()
        elif self.operator == "*":
            return self.mul()
        else:
            raise ValueError(f"{self.operator} not supported")

    def mul(self):
        final = self.values[0]
        for value in self.values[1:]:
            final *= value
        return final

    def add(self):
        final = 0
        for value in self.values:
            final += value
        return final
            


equations = [Equation() for _ in range(len(lines_splitted[0]))]

for line in lines_splitted:
    if line[0] not in ["+", "*"]:
        for i, num in enumerate(line):
            equations[i].add_value(int(num))
    else:
        for i, op in enumerate(line):
            equations[i].set_operator(op)


count = 0
for eq in equations:
    count += eq.calculate()

print(count)