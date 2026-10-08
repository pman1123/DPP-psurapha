PIECES = "PBRQK"
ORTHOGONAL = ((-1, 0), (1, 0), (0, -1), (0, 1))
DIAGONAL = ((-1, -1), (-1, 1), (1, -1), (1, 1))


def parse_board(board):
    """Validate the board and return (rows, king_position).
    Raises ValueError if the board is invalid."""
    if not isinstance(board, str):
        raise ValueError("board must be a string")
    rows = board.splitlines()
    if not rows:
        raise ValueError("empty board")
    size = len(rows)
    for row in rows:
        if len(row) != size:
            raise ValueError("board is not a square")
    kings = []
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == "K":
                kings.append((r, c))
    if len(kings) > 1:
        raise ValueError(f"There are {len(kings)} kings, beyond limit, impossible")
    if not kings:
        raise ValueError("There is no king on the board")
    return rows, kings[0]


def find_attackers(board):
    """Return a list of (piece, row, col) that can capture the King."""
    rows, (kr, kc) = parse_board(board)
    size = len(rows)
    attackers = []

    def inside(r, c):
        return 0 <= r < size and 0 <= c < size

 
    for dc in (-1, 1):
        r, c = kr + 1, kc + dc
        if inside(r, c) and rows[r][c] == "P":
            attackers.append(("P", r, c))

   
    def scan(directions, allowed):
        for dr, dc in directions:
            r, c = kr + dr, kc + dc
            while inside(r, c):
                ch = rows[r][c]
                if ch in PIECES:
                    if ch in allowed:
                        attackers.append((ch, r, c))
                    break  # path is blocked by this piece
                r += dr
                c += dc

    scan(ORTHOGONAL, "RQ")
    scan(DIAGONAL, "BQ")
    return attackers


def checkmate(board):
    """Print Success if the King is in check, Fail if not, Error if invalid."""
    try:
        attackers = find_attackers(board)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print("Success" if attackers else "Fail")
