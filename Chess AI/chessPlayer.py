from chessPlayer_tree import tree
import copy
from random import randint #This is in the case of a tie if multiple moves have the same score. This avoids just taking the first move, which I found
			   #to result in no board presence, but only packing one side of the board

def GetPlayerPositions(board, player):
	pos = []
	for i in range(0, len(board)):
		if (board[i] - player >=0 and board[i] - player <=5):
			pos  = pos + [i]

	return pos

def setBoard():
	board = [0 for i in range(0, 64)]
	for i in range(8, 16):
		board[i] = 10 + 0
	board[0] = 10 + 3
	board[7] = 10 + 3
	board[1] = 10 + 1
	board[6] = 10 + 1
	board[2] = 10 + 2
	board[5] = 10 + 2
	board [3] = 10 + 5
	board [4] = 10 + 4

	for i in range(48, 56):
		board[i] = 20 + 0
	board[56] = 20 + 3
	board[63] = 20 + 3
	board[57] = 20 + 1
	board[62] = 20 + 1
	board[58] = 20 + 2
	board[61] = 20 + 2
	board[59] = 20 + 5
	board[60] = 20 + 4

	return board

def printBoard(board):
   accum="---- BLACK SIDE ----\n"
   max=63
   for j in range(0,8,1):
      for i in range(max-j*8,max-j*8-8,-1):
         accum=accum+'{0: <5}'.format(board[i])
      accum=accum+"\n"
   accum=accum+"---- WHITE SIDE ----"
   print accum
   return True

def genLeftEdge():
	return [i for i in range(0, 57, 8)]

def genRightEdge():
	return [i for i in range(7, 64, 8)]

def genUpEdge():
	return [i for i in range(0, 8)]
def genDownEdge():
	return [i for i in range(56, 64)]

def GetPieceLegalMoves(board, position):
	if (board[position] == 0):
		return []

	if (board[position] - 10 >= 0 and board[position] - 10 <= 5):
		player = 10
	elif (board[position] - 20 >= 0 and board[position] - 20 <=5):
		player = 20
	else:
		return []

	if (player == 10):
		opp = 20
	else:
		opp = 10

	if (player == 10):
		mover = 1
	else:
		mover = -1

	moves = []
	otherPos = GetPlayerPositions(board, opp)
	myPos = GetPlayerPositions(board, player)
	led = genLeftEdge()
	red = genRightEdge()
	ued = genUpEdge()
	ded = genDownEdge()
	if (board[position] -player == 0): # pawn
		#checking to attack:
		if (position not in led):
			if ((position + (mover*8) - 1) in otherPos):
				moves = moves + [position + (mover*8) - 1]
		if (position not in red):
			if ((position + (mover*8) + 1) in otherPos):
				moves = moves + [position + (mover*8) + 1]
		#check regular move:
		potMove = position + mover*8
		if (potMove < 0 or potMove > 63 or (potMove in myPos) or (potMove in otherPos)):
			return moves
		else:
			moves = moves + [potMove]

		return moves

	if (board[position] - player == 1): #knight
		#Going up:
		if ((position - 16) >= 0):
			#going left:
			if (position not in led):
				pot = position - 16 - 1
				if (board[pot] == 0 or (pot in otherPos)):
					moves = moves + [pot]
			#goint right:
			if (position not in red):
				pot = position - 16 + 1
				if (board[pot] == 0 or (pot in otherPos)):
					moves = moves + [pot]

		#Going down:
		if ((position + 16) < 64):
			#going left:
			if (position not in led):
				pot = position + 16 - 1
				if (board[pot] == 0 or (pot in otherPos)):
					moves = moves + [pot]
			#going right:
			if (position not in red):
				pot = position + 16 +1
				if (board[pot] == 0 or (pot in otherPos)):
					moves = moves + [pot]
		#Going Left:
		if((position not in led) and ((position - 1) not in led)):
			#Going up:
			if (position not in ued):
				pot = position - 2 - 8
				if (board[pot] == 0 or (pot in otherPos)):
					moves = moves + [pot]
			#Going down:
			if (position not in ded):
				pot = position - 2 + 8
				if (board[pot] == 0 or (pot in otherPos)):
					moves = moves + [pot]
		
		#Going Right:
		if ((position not in red) and ((position + 1) not in red)):
			#Going upt:
			if (position not in ued):
				pot = position + 2 - 8
				if (board[pot] == 0 or (pot in otherPos)):
					moves = moves + [pot]
			if (position not in ded):
				pot = position + 2 + 8
				if (board[pot] == 0 or (pot in otherPos)):
					moves = moves + [pot]

		return moves 
	if (board[position] - player == 2): #bishop
		#upperleft:
		cur = position
		while((cur not in ued) and (cur not in led)):
			cur = cur - 8 - 1
			if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break

		#upper-right
		cur = position
		while((cur not in ued) and (cur not in red)):
			cur = cur - 8 + 1
			if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break

		#lower-left
		cur = position
		while((cur not in ded) and (cur not in led)):
			cur = cur + 8 - 1
			if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break
	
		#lower-right
		cur = position
		while((cur not in ded) and (cur not in red)):
			cur = cur + 8 + 1
			if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break

		return moves
	if (board[position] - player == 3): #rook
		#left:
		cur = position
		while(cur not in led):
			cur = cur - 1
			if (board[cur] == 0):
				moves = moves + [cur]
			if (cur in otherPos):
				moves = moves + [cur]
				break
			if (cur in myPos):
				break

		cur = position
		#right:
		while(cur not in red):
			cur = cur + 1
			if (board[cur] == 0):
				moves = moves + [cur]
			if (cur in otherPos):
				moves = moves + [cur]
				break
			if (cur in myPos):
				break
		cur = position
		#up:
		while(cur not in ued):
			cur = cur - 8
			if (board[cur] == 0):
				moves = moves + [cur]
			if (cur in otherPos):
				moves = moves + [cur]
				break
			if (cur in myPos):
				break
		cur = position
		#down:
		while(cur not in ded):
			cur = cur + 8
			if (board[cur] == 0):
				moves = moves + [cur]
			if (cur in otherPos):
				moves = moves + [cur]
				break
			if (cur in myPos):
				break
		return moves

	if (board[position] - player == 4): #queen
		#left:
                cur = position
                while(cur not in led):
                        cur = cur - 1
                        if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break

                cur = position
                #right:
                while(cur not in red):
                        cur = cur + 1
                        if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break
                cur = position
                #up:
                while(cur not in ued):
                        cur = cur - 8
                        if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break
                cur = position
                #down:
                while(cur not in ded):
                        cur = cur + 8
                        if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break
	
		 #upperleft:
                cur = position
                while((cur not in ued) and (cur not in led)):
                        cur = cur - 8 - 1
                        if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break

                #upper-right
                cur = position
                while((cur not in ued) and (cur not in red)):
                        cur = cur - 8 + 1
                        if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break

                #lower-left
                cur = position
                while((cur not in ded) and (cur not in led)):
                        cur = cur + 8 - 1
                        if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break

                #lower-right
                cur = position
                while((cur not in ded) and (cur not in red)):
                        cur = cur + 8 + 1
                        if (board[cur] == 0):
                                moves = moves + [cur]
                        if (cur in otherPos):
                                moves = moves + [cur]
                                break
                        if (cur in myPos):
                                break

                return moves

	
	if (board[position] - player == 5): #king
		#up
		if (position not in ued):
			pot = position - 8
			if (board[pot] == 0 or (pot in otherPos)):
				moves = moves + [pot]
			
			#upper-right
			if (position not in red):
				pot = position - 8 + 1
				if (board[pot] == 0 or (pot in otherPos)):
					moves = moves + [pot]
			#upper-left
			if (position not in led):
				pot = position - 8 - 1
				if (board[pot] == 0 or (pot in otherPos)):
					moves = moves + [pot]	
		#down
		if (position not in ded):
			pot = position + 8
			if (board[pot] == 0 or (pot in otherPos)):
				moves = moves + [pot]
					
			#lower-right
                        if (position not in red):
                                pot = position + 8 + 1
                                if (board[pot] == 0 or (pot in otherPos)):
                                        moves = moves + [pot]
                        #lower-left
                        if (position not in led):
                                pot = position + 8 - 1
                                if (board[pot] == 0 or (pot in otherPos)):
                                        moves = moves + [pot]

		#left
		if (position not in led):
			pot = position - 1
			if (board[pot] == 0 or (pot in otherPos)):
				moves = moves + [pot]
		#right
		if (position not in red):
			pot = position + 1
			if (board[pot] == 0 or (pot in otherPos)):
				moves = moves + [pot]


		return moves

def belongsTo(board, position):
	if (isWhite(board, position)):
		return 10
	if (isBlack(board, position)):
		return 20
	return 0

def getOpponent(player):
	if (player == 10):
		return 20
	if (player == 20):
		return 10
	return -1
def IsPositionUnderThreat(board, position, player):
	if (player == 10):
		opponent = 20
	elif(player == 20):
		opponent = 10
	else:
		return False

	if (board[position] == 0):
		return False
	if (belongsTo(board, position) == opponent):
		return False
	opPos = GetPlayerPositions(board, opponent)
	for i in opPos:
		moves = GetPieceLegalMoves(board, i)
		if position in moves:
			return True

	return False

def getThreateningPiece(board, position, player):
	if (player == 10):
		opponent = 20
	elif(player == 20):
		opponent = 10
	else:
		return False
	threat = []
	if (IsPositionUnderThreat(board, position, player)):
		opPos = GetPlayerPositions(board, opponent)
		for i in opPos:
			moves = GetPieceLegalMoves(board, i)
			if position in moves:
				threat = threat + [board[i]]
	return threat
		
def IsPositionProtected(board, position, player):
	if (board[position] == 0):
		return False
	opponent = getOpponent(player)
	if (belongsTo(board, position) == opponent):
		return False
	boardCopy = list(board)
	boardCopy[position] = 0
	pos = GetPlayerPositions(boardCopy, player)
	for i in pos:
		moves = GetPieceLegalMoves(boardCopy, i)
		if position in moves:
			return True

def isWhite(board, position):
	if (board[position] - 10 >= 0 and board[position] - 10 <= 5):
		return True
	return False

def isBlack(board, position):
	if (board[position] - 20 >= 0 and board[position] - 20 <= 5):
		return True
	return False	

def GetPos(board, piece):
	for i in range(0, len(board)):
		if (board[i] == piece):
			return i
	return -1

def evalBoard(board, player):
	#player is an argument. If evalBoard is positive, board is in player's favour
	#evalBoard is negative, board is in opponent's favour
	rval = 0
	for i in range(0, len(board)):
		rval = rval + pieceEval(board[i], player)

        return rval
def threatLevel(board, player):
	rval = 0
	opponent = getOpponent(player)
	for i in range(0, len(board)):
	 	if (IsPositionUnderThreat(board, i, player)): #opponent is threatening player
                        if (IsPositionProtected(board, i, player)):
                                threat = getThreateningPiece(board, i, player)
                                minThreat = min(threat) #if position is under threat, they'll use the weakest piece to get you
                                minThreat = minThreat - opponent
                                rval = rval - ((pieceEval(minThreat, player) +  pieceEval(board[i], player))/2)
                        else:
                                rval = rval - (pieceEval(board[i], player)/2)
                elif (IsPositionUnderThreat(board, i, opponent)): #player is threatening opponent and opponent is not threatening player
                        if (IsPositionProtected(board, i, opponent)):
                                threat = getThreateningPiece(board, i, opponent)
                                minThreat = min(threat)
                                minThreat = minThreat - player
                                valueDiff = pieceEval(minThreat, player) + pieceEval(board[i], player)
                                if (valueDiff <= 0): 
                                        rval = rval - valueDiff #because this move adds value, and since valueDiff is -, we want to make it +
                        else:
                                rval = rval - (pieceEval(board[i], player))/2 #- as it is an opponent's piece which is negative

        return rval


def pieceEval(piece, player):
	if (player == 10):
		opponent = 20
	elif(player == 20):
		opponent = 10
	else:
		return False

	if ((piece - player >= 0) and (piece - player <=5)):
		mult = 1.0 #treat our pieces as positive
		owner = player
	elif((piece - opponent) >= 0 and (piece - opponent)<=5):
		mult = -1.0#treat opponent's piece as negative
		owner = opponent
	else:
		return 0

	abspiece = piece - owner #actual piece value

	if (abspiece == 0):
		return mult*10 #pawn
	if (abspiece == 1):
		return mult*30 #knight
	if (abspiece == 2):
		return mult*30 #bishop
	if (abspiece == 3):
		return mult*50 #rook value
	if (abspiece == 4):
		return mult*90 #queen value
	if (abspiece == 5):
		return mult*900 #king value - very high
	return 0

#checks if ANY piece is under threat:
def underThreat(board, player):
	for i in range(0, len(board)):
		if (IsPositionUnderThreat(board, i,  player)):
			return True

def canAttack(board, player):
	opponent = getOpponent(player)
	return underThreat(board, opponent)

def chessPlayer(board, player):
	if (len(board)!=64 or (player <> 10 and player <> 20)):
		return [False, [], [], []]
	for i in range(0, len(board)):
		if (not(isBlack(board, i) or  isWhite(board, i) or (board[i] ==0))):
			return [False, [], [], []]
	candidates = []
	opponent = getOpponent(player)
	root = tree(-1) #an arbitrary value. Made to be the head of the eval tree so all board moves can be represented as one tree
	kingPos = GetPos(board, player + 5)
	check = IsPositionUnderThreat(board, kingPos, player)
	if (check): #try to get out of check to not lose
		L = GetPlayerPositions(board, player)
		for i in L:
			legal = GetPieceLegalMoves(board, i)
			for j in legal: 
				boardCopy = list(board)
				boardCopy[j] = boardCopy[i]
				boardCopy[i] = 0
				kingPos = GetPos(boardCopy, player + 5)
				threat = IsPositionUnderThreat(boardCopy, kingPos, player)
				if (not threat):
					score = evalBoard(boardCopy, player)
					if(IsPositionUnderThreat(boardCopy, j, player)):
						score = score - (pieceEval(boardCopy[j], player)) #this is so we don't sacrifice a more expensive piece
					candidates = candidates + [[[i, j], score]]
	
					
	else:
		L = GetPlayerPositions(board, player)
		for i in L:
			legal = GetPieceLegalMoves(board, i)
			for j in legal:
				tmp = tree(-1)
				boardCopy = list(board)
				boardCopy[j] = boardCopy[i]
				boardCopy[i] = 0
				#we set maximizing player to false here because we are maximizing the score in this section currently. Need to 
				moveScore = genMoveTree(boardCopy, player, 2, False, -10000, 10000, tmp)
				tmp.store[0] = moveScore
				root.AddSuccessor(copy.copy(tmp)) #This tree is to keep a record of all the scores from the board states evaluated by genMove Tree
				candidates = candidates + [[[i, j], moveScore]]
	if (candidates == []):
		return [False, [], [], []]
	#Move cannot put you in check:
	for i in range(0, len(candidates)):
		fromPos = candidates[i][0][0]
		toPos = candidates[i][0][1]
		boardCopy = list(board)
		boardCopy[toPos] = boardCopy[fromPos]
		boardCopy[fromPos] = 0
		kingPos = GetPos(boardCopy, player + 5)
		if (IsPositionUnderThreat(boardCopy, kingPos, player)):
			candidates[i][1] = -100000
	cop = list(candidates)
	candidates = []
	for i in cop:
		if i[1] != -100000:
			candidates = candidates + [i]

	bestMove = candidates[0]
	rest = candidates[1:]
	for k in rest:
		if k[1] > bestMove[1]:
			bestMove = k
	#in the case where multiple pieces have the same score, we don't want to choose randomly. Choose the spots closer to the centre, and prioritieze control there
	#This also tests for if we are threatening opponents and whether we are going to a threatening spot
	repeats = []
	for i in candidates:
		if i[1] == bestMove[1]:
			repeats = repeats + [i]
	for j in repeats:
		boardCopy = list(board)
		boardCopy[j[0][1]] = boardCopy[j[0][0]]
		boardCopy[j[0][0]] = 0
		if (IsPositionUnderThreat(boardCopy, j[0][1], player)):
			j[1] = j[1] - pieceEval(board[j[0][0]], player) #minus points if the place is under threat
		if(belongsTo(board, j[0][1]) == opponent):
			j[1] = j[1] - pieceEval(board[j[0][0]], player) #add points (sinse opponent piece is negative) if we capture a piece here
			
		if (j[0][1] == 27 or j[0][1] == 28 or j[0][1] == 35 or j[0][1] == 36):
			j[1] = j[1] + 1
		elif(j[0][1] == 26 or j[0][1] == 29 or j[0][1] == 34 or j[0][1] == 37):
			j[1]= j[1] + 0.5

	bestMove = repeats[0]
	rest = repeats[1:]
	for k in rest:
		if k[1] > bestMove[1]:
			bestMove = k

	final = []
	for i in repeats:
		if i[1] == bestMove[1]:
			final = final + [i]

	rand = randint(0, len(final) - 1) #this is to avoid repetitive results, as taking just the first move with the best score results in no board presence, 
					  # but rather, only moves the pieces with a lower number
	bestMove = final[rand]
	evalTree = root.Get_LevelOrder()
	if (evalTree == [-1]): #this means nothing was added to the evalTree
		evalTree = None
	return [True, bestMove[0], candidates, evalTree]	

#This function looks at all legal moves, and recursively evaluates scores for each possible board state, to return
#a score to the move in chessPlayer. This move is calculated with a Minimax algorithm, to minimize loss, and play the "safe route"
#a tree is submitted to keep a record of all the game states, so that there is a record of this scoring process and the different
#gamestates
def genMoveTree(board, player, depth, isMax, alpha, beta, scoreTree):
	if (depth == 0):
		state = evalBoard(board, player)
		return state
	if (player == 10):
		opponent= 20
	elif(player == 20):
		opponent = 10
	else:
		return False
	if (isMax):
		bestMove = -9999
		L = GetPlayerPositions(board, player)
		for i in L:
			legal = GetPieceLegalMoves(board, i)
			for j in legal:
				 #we only want to keep track of this record if the depth is not too high, to save memory, which is why
				#tree is only added to if depth >=2
				tmp= tree(-1)
				boardCopy = list(board)
				boardCopy[j] = boardCopy[i]
				boardCopy[i] = 0
				bestMove = max([bestMove, genMoveTree(boardCopy, player, depth - 1, False, alpha, beta, tmp)])
				if (depth >=2):
					tmp.store[0] = bestMove
					scoreTree.AddSuccessor(copy.copy(tmp))
				alpha = max([alpha, bestMove])
				if (beta <= alpha):
					return bestMove
		
		return bestMove
	else:
		bestMove = 9999
		L = GetPlayerPositions(board, opponent)
		for i in L:
			legal = GetPieceLegalMoves(board, i)
			for j in legal:
				tmp = tree(-1)
				boardCopy = list(board)
				boardCopy[j] = boardCopy[i]
				boardCopy[i] = 0
				bestMove = min([bestMove, genMoveTree(boardCopy, player, depth-1, True, alpha, beta, tmp)])
				if (depth >=2):
					tmp.store[0] = bestMove
					scoreTree.AddSuccessor(copy.copy(tmp))
				beta = min([beta, bestMove])
				if (beta <= alpha):
					return bestMove
		return bestMove
