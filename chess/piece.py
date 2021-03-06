'''
Piece module for Computer Science chess final project

Contains all methods related to piece movement 
'''
from chess.utils import *

class Piece:
	piece_type = "Null"
	color = "Null"
	position = "Null"
	
	def __init__(self, piece_type, color, position): 
		self.piece_type = piece_type
		self.color = color
		self.position = position
		''' piece_type is a string that describes which piece it is.
			color refers to which player the piece belongs (black or white)
			position describes the location of the piece on the board (e.g. a5)'''
		
	def get_moves(self, board):
		if self.piece_type == "pawn":
			return self.get_pawn_moves(board)
		elif self.piece_type == "rook":
			return self.get_rook_moves(board)
		elif self.piece_type == "knight":
			return self.get_knight_moves(board)
		elif self.piece_type == "bishop":
			return self.get_bishop_moves(board)
		elif self.piece_type == "queen":
			return self.get_queen_moves(board)
		elif self.piece_type == "king":
			return self.get_king_moves(board)
		
		else:
			return []
		
		return moves
	
	def get_pawn_moves(self, game):
		moves = []
		coords = algebraic_to_cartesian(self.position)
		if self.color == "white":
			av1 = cartesian_to_algebraic([coords[0] - 1, coords[1] + 1])
			av2 = cartesian_to_algebraic([coords[0] + 1, coords[1] + 1])
			av3 = cartesian_to_algebraic([coords[0], coords[1] + 1])
		if self.color == "black":
			av1 = cartesian_to_algebraic([coords[0] - 1, coords[1] - 1])
			av2 = cartesian_to_algebraic([coords[0] + 1, coords[1] - 1])
			av3 = cartesian_to_algebraic([coords[0], coords[1] - 1])
			
		# av = "attack vector"
		
		if game.piece_at(av3).color == "Null":
			moves.append(self.position +  av3)
		try:
			if game.piece_at(av1).color != "Null" and game.piece_at(av1).color != self.color:
				moves.append(self.position + av1)
			if game.piece_at(av2).color != "Null" and game.piece_at(av2).color != self.color:
				moves.append(self.position + av2)
		
		except:
			pass
			
		if self.color == "white" and coords[1] == 1 and game.piece_at(av3).piece_type == "Null" and game.piece_at(cartesian_to_algebraic([coords[0], coords[1] + 2])).piece_type == "Null":
			moves.append(self.position + cartesian_to_algebraic([coords[0], 3]))
		if self.color == "black" and coords[1] == 6 and game.piece_at(av3).piece_type == "Null" and game.piece_at(cartesian_to_algebraic([coords[0], coords[1] - 2])).piece_type == "Null":
			moves.append(self.position + cartesian_to_algebraic([coords[0], 4]))
		
		return moves
	
	def get_rook_moves(self, game):
		moves = []
		coords = algebraic_to_cartesian(self.position)
		
		for i in range(1,8):
			if coords[1] + i > 7 or game.piece_at(cartesian_to_algebraic([coords[0], coords[1] + i])).color == self.color:
				break
			moves.append(self.position + cartesian_to_algebraic([coords[0], coords[1] + i]))
			if game.piece_at(cartesian_to_algebraic([coords[0], coords[1] + i])).piece_type != "Null":
				break
		
		for i in range(1,8):
			if coords[1] - i < 0 or game.piece_at(cartesian_to_algebraic([coords[0], coords[1] - i])).color == self.color:
				break
			moves.append(self.position + cartesian_to_algebraic([coords[0], coords[1] - i]))
			if game.piece_at(cartesian_to_algebraic([coords[0], coords[1] - i])).piece_type != "Null":
				break
		
		for i in range(1,8):
			if coords[0] + i > 7 or game.piece_at(cartesian_to_algebraic([coords[0] + i, coords[1]])).color == self.color:
				break
			moves.append(self.position + cartesian_to_algebraic([coords[0]+ i, coords[1]]))
			if game.piece_at(cartesian_to_algebraic([coords[0] + i, coords[1]])).piece_type != "Null":
				break
		
		for i in range(1,8):
			if coords[0] - i < 0 or game.piece_at(cartesian_to_algebraic([coords[0] - i, coords[1]])).color == self.color:
				break
			moves.append(self.position + cartesian_to_algebraic([coords[0] - i, coords[1]]))
			if game.piece_at(cartesian_to_algebraic([coords[0] - i, coords[1]])).piece_type != "Null":
				break

		return moves
		
	def get_bishop_moves(self, game):
		moves = []
		coords = algebraic_to_cartesian(self.position)
		
		for i in range(1,8):
			if coords[1] + i > 7 or coords[0] + i > 7 or game.piece_at(cartesian_to_algebraic([coords[0] + i, coords[1] + i])).color == self.color:
				break
			moves.append(self.position + cartesian_to_algebraic([coords[0] + i, coords[1] + i]))
			if game.piece_at(cartesian_to_algebraic([coords[0] + i, coords[1] + i])).piece_type != "Null":
				break
		
		for i in range(1,8):
			if coords[1] - i < 0 or coords[0] - i < 0 or game.piece_at(cartesian_to_algebraic([coords[0] - i, coords[1] - i])).color == self.color:
				break
			moves.append(self.position + cartesian_to_algebraic([coords[0] - i, coords[1] - i]))
			if game.piece_at(cartesian_to_algebraic([coords[0] - i, coords[1] - i])).piece_type != "Null":
				break
		
		for i in range(1,8):
			if coords[0] + i > 7 or coords[1] - i < 0 or game.piece_at(cartesian_to_algebraic([coords[0] + i, coords[1] - i])).color == self.color:
				break
			moves.append(self.position + cartesian_to_algebraic([coords[0] + i, coords[1] - i]))
			if game.piece_at(cartesian_to_algebraic([coords[0] + i, coords[1] - i])).piece_type != "Null":
				break
		
		for i in range(1,8):
			if coords[0] - i < 0 or coords[1] + i > 7 or game.piece_at(cartesian_to_algebraic([coords[0] - i, coords[1] + i])).color == self.color:
				break
			moves.append(self.position + cartesian_to_algebraic([coords[0] - i, coords[1] + i]))
			if game.piece_at(cartesian_to_algebraic([coords[0] - i, coords[1] + i])).piece_type != "Null":
				break

		return moves
	
	def get_queen_moves(self, game):
		bish_moves = self.get_bishop_moves(game)
		rook_moves = self.get_rook_moves(game)
		
		return bish_moves + rook_moves
		
	def get_knight_moves(self, game):
		coords = algebraic_to_cartesian(self.position)
		moves = []
		
		if coords[0] + 2 <= 7 and coords[1] + 1 <= 7 and game.piece_at(cartesian_to_algebraic([coords[0] + 2, coords[1] + 1])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] + 2, coords[1] + 1]))
		if coords[0] + 1 <= 7 and coords[1] + 2 <= 7 and game.piece_at(cartesian_to_algebraic([coords[0] + 1, coords[1] + 2])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] + 1, coords[1] + 2]))
		if coords[0] - 1 >= 0 and coords[1] + 2 <= 7 and game.piece_at(cartesian_to_algebraic([coords[0] - 1, coords[1] + 2])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] - 1, coords[1] + 2]))
		if coords[0] - 2 >= 0 and coords[1] + 1 <= 7 and game.piece_at(cartesian_to_algebraic([coords[0] - 2, coords[1] + 1])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] - 2, coords[1] + 1]))
		if coords[0] + 2 <= 7 and coords[1] - 1 >= 0 and game.piece_at(cartesian_to_algebraic([coords[0] + 2, coords[1] - 1])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] + 2, coords[1] - 1]))
		if coords[0] + 1 <= 7 and coords[1] - 2 >= 0 and game.piece_at(cartesian_to_algebraic([coords[0] + 1, coords[1] - 2])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] + 1, coords[1] - 2]))
		if coords[0] - 1 >= 0 and coords[1] - 2 >= 0 and game.piece_at(cartesian_to_algebraic([coords[0] - 1, coords[1] - 2])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] - 1, coords[1] - 2]))
		if coords[0] - 2 >= 0 and coords[1] - 1 >= 0 and game.piece_at(cartesian_to_algebraic([coords[0] - 2, coords[1] - 1])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] - 2, coords[1] - 1]))
			
		return moves
	
	def get_king_moves(self, game):
		coords = algebraic_to_cartesian(self.position)
		moves = []
		
		if coords[0] + 1 <= 7 and game.piece_at(cartesian_to_algebraic([coords[0] + 1, coords[1]])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] + 1, coords[1]]))
		if coords[1] + 1 <= 7 and game.piece_at(cartesian_to_algebraic([coords[0], coords[1] + 1])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0], coords[1] + 1]))
		if coords[0] - 1 >= 0 and game.piece_at(cartesian_to_algebraic([coords[0] - 1, coords[1]])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] - 1, coords[1]]))
		if coords[1] - 1 >= 0 and game.piece_at(cartesian_to_algebraic([coords[0], coords[1] - 1])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0], coords[1] - 1]))
		if coords[0] + 1 <= 7 and coords[1] + 1 <= 7 and game.piece_at(cartesian_to_algebraic([coords[0] + 1, coords[1] + 1])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] + 1, coords[1] + 1]))
		if coords[0] - 1 >= 0 and coords[1] + 1 <= 7 and game.piece_at(cartesian_to_algebraic([coords[0] - 1, coords[1] + 1])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] - 1, coords[1] + 1]))
		if coords[0] + 1 <= 7 and coords[1] - 1 >= 0 and game.piece_at(cartesian_to_algebraic([coords[0] + 1, coords[1] - 1])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] + 1, coords[1] - 1]))
		if coords[0] - 1 >= 0 and coords[1] - 1 >= 0 and game.piece_at(cartesian_to_algebraic([coords[0] - 1, coords[1] - 1])).color != self.color:
			moves.append(self.position + cartesian_to_algebraic([coords[0] - 1, coords[1] - 1]))
		
		return moves
