


from collections import deque



def knights(A, B, C, D, E, F):
    dx = [-2, -1, 1, 2, -2, -1, 1, 2] 
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    def valid_moves(x, y):
        for i in range(8):
            new_pos_x = x + dx[i]
            new_pos_y = y + dy[i]


            if 1 <= new_pos_x <= A and 1 <= new_pos_y <= B:
                yield new_pos_x, new_pos_y



    q = deque([(C, D, 0)])
    visited = [[False for _ in range(B + 1)] for _ in range(A + 1)]
    visited[C][D] = True

    while q:
        x, y, moves = q.popleft()
        if x == E and y == F:
            return moves
        for new_pos_x, new_pos_y in valid_moves(x, y):
            if not visited[new_pos_x][new_pos_y]:
                visited[new_pos_x][new_pos_y] = True
                q.append((new_pos_x, new_pos_y, moves + 1))
    return -1


