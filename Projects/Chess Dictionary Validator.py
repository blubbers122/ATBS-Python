board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking',
    "3f": 'wbishop',
    "3h": 'wknight',
    "4a": 'wknight',
    "4b": 'wbishop',
    "6e": 'bbishop'
}


def isValidChessBoard(board):
    bPieceList = {}
    wPieceList = {}
    pieceLimit = {
        'pawn': 8,
        'knight': 2,
        'bishop': 2,
        'rook': 2,
        'queen': 1,
        'king': 1
    }
    pieces = pieceLimit.keys()
    for piece in pieces:
        bPieceList[piece] = 0
        wPieceList[piece] = 0
    for k, v in board.items():
        if len(k) != 2:  # grid key must be 2 characters
            return False
        elif not(0 < int(k[0]) < 9) or not("a" <= k[1] < "i"):  # grid key chars must be 1-8 and a-h
            return False
        if v[0] == "b" or v[0] == "w" and v[1:] in pieces:  # piece code must be b or w followed by a piece name
            result = countPieces(v, pieceLimit, wPieceList, bPieceList)
            if not result:  # only returns a failing return from countPieces()
                return result
        else:
            return False
    return True  # returns passed test


def countPieces(v, pieceLimit, wPieceList, bPieceList):
    color = v[0]
    currentPiece = v[1:]
    limit = pieceLimit[currentPiece]
    if color == "w":
        chosenList = wPieceList
    else:
        chosenList = bPieceList
    chosenList[currentPiece] += 1  # increments
    return not chosenList[currentPiece] > limit  # tells validator if the current piece count exceeds the limit


print(isValidChessBoard(board))
