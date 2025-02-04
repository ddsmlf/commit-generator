def is_valid_move(knight_pos, new_pos, visited):
    x, y = knight_pos
    dx, dy = abs(new_pos[0] - x), abs(new_pos[1] - y)
    return (dx * dx + dy * dy) == 5 and (new_pos not in visited)

def count_available_moves(knight_pos, available_squares):
    x, y = knight_pos
    moves = [
        (x+2, y+1), (x+2, y-1),
        (x-2, y+1), (x-2, y-1),
        (x+1, y+2), (x+1, y-2),
        (x-1, y+2), (x-1, y-2)
    ]
    return sum(1 for pos in moves if pos in available_squares)

def solve_knight_tour(board_size):
    visited = set()
    path = []
    
    def backtrack(positions):
        current_pos = positions[-1] if positions else None
        next_positions = []
        
        if len(visited) == board_size * board_size:
            return positions
        
        for move in count_available_moves(current_pos, available_squares=available_squares):
            temp_visited = visited.copy()
            temp_path = path.copy()
            temp_path.append(move)
            temp_visited.add(move)
            next_positions.append((move, temp_path, temp_visited))
        
        if next_positions:
            best_move, best_path, best_visited = max(next_positions, key=lambda x: len(x[2]))
            return backtrack(best_path + [best_move])
        else:
            return None
    
    available_squares = set()
    
    for i in range(board_size):
        for j in range(board_size):
            available_squares.add((i, j))
    
    start_pos = (0, 0)
    if is_valid_move(start_pos, start_pos, visited):
        initial_path = [start_pos]
        initial_visited = {start_pos}
        result = backtrack(initial_path)
        if result:
            return '\n'.join(f'{pos[0]}-{pos[1]}' for pos in result)
    
    print("No solution found.")