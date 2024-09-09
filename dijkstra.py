def min_effort_bfs(puzzle):
    m, n = len(puzzle), len(puzzle[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # List to act as a priority queue with elements (effort, row, col)
    pq = [(0, 0, 0)]
    efforts = [[float('inf')] * n for _ in range(m)]
    efforts[0][0] = 0
    
    while pq:
        # Sort the list and pop the smallest element
        pq.sort()
        current_effort, row, col = pq.pop(0)
        
        if row == m - 1 and col == n - 1:  # reached destination
            return current_effort
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < m and 0 <= new_col < n:
                # Calculate effort to the new cell
                new_effort = max(current_effort, abs(puzzle[new_row][new_col] - puzzle[row][col]))
                
                # If this path offers a smaller effort, update and push to the queue
                if new_effort < efforts[new_row][new_col]:
                    efforts[new_row][new_col] = new_effort
                    pq.append((new_effort, new_row, new_col))

# Example usage:
puzzle = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
print(min_effort_bfs(puzzle))  # Expected output: 2