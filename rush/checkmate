# checkmate.py

def checkmate(board):
    def find_king(board):
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == 'K':
                    return r, c
        return None  # No King found

    def is_attacked_by_pawn(board, king_pos):
        r, c = king_pos
        pawn_attacks = [(r - 1, c - 1), (r - 1, c + 1)]  # Pawns attack diagonally
        for rr, cc in pawn_attacks:
            if 0 <= rr < n and 0 <= cc < n and board[rr][cc] == 'P':
                return True
        return False

    def is_attacked_by_rook_or_queen(board, king_pos):
        r, c = king_pos
        # Check horizontally and vertically
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            rr, cc = r + dr, c + dc
            while 0 <= rr < n and 0 <= cc < n:
                if board[rr][cc] != '.':
                    if board[rr][cc] in ('R', 'Q'):  # Rook or Queen
                        return True
                    break  # Blocked by another piece
                rr += dr
                cc += dc
        return False

    def is_attacked_by_bishop_or_queen(board, king_pos):
        r, c = king_pos
        # Check diagonally
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            rr, cc = r + dr, c + dc
            while 0 <= rr < n and 0 <= cc < n:
                if board[rr][cc] != '.':
                    if board[rr][cc] in ('B', 'Q'):  # Bishop or Queen
                        return True
                    break  # Blocked by another piece
                rr += dr
                cc += dc
        return False

    def is_attacked_by_knight(board, king_pos):
        r, c = king_pos
        knight_moves = [
            (r - 2, c - 1), (r - 2, c + 1),
            (r - 1, c - 2), (r - 1, c + 2),
            (r + 1, c - 2), (r + 1, c + 2),
            (r + 2, c - 1), (r + 2, c + 1)
        ]
        for rr, cc in knight_moves:
            if 0 <= rr < n and 0 <= cc < n and board[rr][cc] == 'N':  # Knight
                return True
        return False

    # Prepare the board
    board = board.splitlines()
    n = len(board)

    # Find the King
    king_pos = find_king(board)
    if not king_pos:
        print("Error: No King found.")
        return

    # Check if the King is in check
    if (is_attacked_by_pawn(board, king_pos) or
        is_attacked_by_rook_or_queen(board, king_pos) or
        is_attacked_by_bishop_or_queen(board, king_pos) or
        is_attacked_by_knight(board, king_pos)):
        print("Success")
    else:
        print("Fail")
