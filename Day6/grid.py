def read_stdin(starter = None):
    from sys import stdin
    grid = {}
    start = None
    row = 1
    for line in stdin:
        for col, item in enumerate(list(line.strip())):
            grid[(row, col+1)] = item
            if item == starter:
                start = (row, col+1)
        row += 1
    if start is not None:
        return grid, start
    return grid