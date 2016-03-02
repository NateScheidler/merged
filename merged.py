# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:17:50 2016

@author: Nate
"""
import numpy as np


class Piece:
    tile_1 = 0
    tile_2 = 0
    def Piece(self, tile_1, tile_2):
        self.tile_1 = tile_1
        self.tile_2 = tile_2
    def is_singlet(self):
        return self.tile_2 == 0
        
class Board:
    squares = np.zeros([5,5])
    highTile = 2


        
    def list_neighbors(self, tile, pos, known_neighbors):
        neighbors = []        
        for x in [pos.x-1,pos.x+1]:
            for y in [pos.y-1, pos.y+1]:
                if ( self.valid(x,y) and
                self.board[x,y] == tile and
                [x,y] not in known_neighbors):
                        neighbors.append([x,y])
        return neighbors    
    
    def place(self, piece, pos_1 , pos_2):
        if self.squares[pos_1.x,pos_1.y] + self.squares[pos_2.x,pos_2.y] != 0:
            return False
        self.squares[pos_1.x,pos_1.y] = piece.tile_1
        self.squares[pos_2.x,pos_2.y] = piece.tile_2
        # vacuum up triples etc
        # list neighbors of same value
        # 
        possible_neighbors_exist = True
        while(possible_neighbors_exist):
            n = self.list_neighbors(piece.tile_1, pos_1, [])
            for m in n:        
                n.append(self.list_neighbors(piece.tile_1, m, n))
        
        return True

    
    def valid(x,y):
        return -1<x<6 and -1<y<6

    def get_random_piece(self):
        piece = Piece()
        piece.tile_1 = np.random.randint(1,self.highTile+1)
        if(np.random.rand() < 0.5):
            piece.tile_2 = np.random.randint(1,self.highTile+1)
        return piece

class Position:
    x = 0
    y = 0
    def Position(self, x,y):
        self.x = x
        self.y = y




def run():
    board = Board()
    current_piece = board.get_random_piece