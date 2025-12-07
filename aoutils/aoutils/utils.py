__all__ = ["get_lines", "get_lines_splitted"]

def get_lines(filepath):
    return get_lines_splitted(filepath, sep=None)


def get_lines_splitted(filepath, sep=" "):
    lines = []
    with open(filepath, "r") as file:
        for line in file:
            processed_line = line.strip()
            if sep is not None:
                processed_line = processed_line.split(sep)
            processed_line = [x for x in processed_line if x != '']
            lines.append(processed_line)
    return lines