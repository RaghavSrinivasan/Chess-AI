import chessPlayer
from random import randint

board = chessPlayer.setBoard()
done = False
player = 10
opponent = 20
cnt = 0
while (not done):
	chessPlayer.printBoard(board)
	if (player == 20):
		print("Black Player Playing (Random): ")
		L = chessPlayer.GetPlayerPositions(board, player)
		fromPos = randint(0, len(L) - 1)
		fromPos = L[fromPos]
		legal = chessPlayer.GetPieceLegalMoves(board, fromPos)
		while(len(legal) == 0):
			fromPos = randint(0, len(L) - 1)
			fromPos = L[fromPos]
			legal = chessPlayer.GetPieceLegalMoves(board, fromPos)
		toPos = randint(0, len(legal) - 1)
		toPos = legal[toPos]
		if (board[toPos] != 0):
			print("Random's piece " + str(board[toPos]) + " captured " + str(board[fromPos]))
		board[toPos] = board[fromPos]
		board[fromPos] = 0
	if (player == 10):
		print ("White Player Playing: ")
		cnt = cnt + 1
		print ("There have been " + str(cnt) + " moves")
		result = chessPlayer.chessPlayer(board, player)
		if (result[0]):
			if (result[3] == None):
				print "No eval tree was used"
			toprint = result[:3]
			if (result[3] != None):
				toprint = toprint + [result[3]]
			print toprint
			move = result[1]
			if (board[move[1]] != 0):
				print ("Piece " + str(board[move[0]]) + " captured " + str(board[move[1]]))
			board[move[1]] = board[move[0]]
			board[move[0]] = 0
		else:
			print "Programmer, you done goofed"
			break

	kingPos = chessPlayer.GetPos(board, opponent + 5)
	check = chessPlayer.IsPositionUnderThreat(board, kingPos, opponent)
	if (check):
		done = True
		opPieces = chessPlayer.GetPlayerPositions(board, opponent)
		for i in opPieces:
			comeback = chessPlayer.GetPieceLegalMoves(board, i)
			for j in comeback:
				boardCopy = list(board)
				boardCopy[j] = boardCopy[i]
				boardCopy[i] = 0
				kingPos = chessPlayer.GetPos(boardCopy, opponent + 5)
				if (not (chessPlayer.IsPositionUnderThreat(boardCopy, kingPos, opponent))):
					print ("piece " + str(i) + " can go to position " + str(j) + " to stop checkmate")
					done = False
	if (not done):
		if (player == 10):
			player = 20
			opponent = 10
		else:
			player = 10
			opponent = 20

print("Congratulations, player " + str(player) + " wins")

