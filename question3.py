# a) allow Totoshka to pass through the minefield.
def find_safe_path(minefield):
    n = len(minefield)  # Number of rows
    m = len(minefield[0])  # Number of columns

    stack = [(0, 0)]  # Start position
    visited = set()  # Set to track visited positions

    while stack:
        x, y = stack.pop()

        if (x, y) == (n - 1, m - 1):  # Target position reached
            return True

        if (x, y) not in visited and minefield[x][y] == '√':  # Safe position
            visited.add((x, y))

            # Check adjacent cells (up, down, left, right)
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for nx, ny in neighbors:
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                    stack.append((nx, ny))

    return False  # No safe path found


#b) Algorithm for Totoshka and Ally to pass through the minefield.
def find_safe_path_for_totoshka_and_ally(minefield):
    n = len(minefield)  # Number of rows
    m = len(minefield[0])  # Number of columns

    stack = [(0, 0, 'T')]  # Start position for Totoshka
    visited = set()  # Set to track visited positions

    while stack:
        x, y, flag = stack.pop()

        if (x, y) == (n - 1, m - 1):  # Target position reached
            return True

        if (x, y, flag) not in visited and minefield[x][y] == '√':  # Safe position
            visited.add((x, y, flag))

            # Check adjacent cells (up, down, left, right)
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for nx, ny in neighbors:
                if 0 <= nx < n and 0 <= ny < m and (nx, ny, flag) not in visited:
                    opposite_flag = 'A' if flag == 'T' else 'T'  # Flag for the opposite character
                    stack.append((nx, ny, opposite_flag))

    return False  # No safe path found


