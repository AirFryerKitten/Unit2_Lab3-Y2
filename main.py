#Jonas York
#U2 L3
#Making a Player vs Computer game of Tic Tac Toe.

from tic_tac_toe import *
import random

def rules(): #explains rules
  print("RULES".center(30,"~"))
  print("""
  Welcome to TictacToe!
  The rules are simple. 
  You play as \'X\'. I play as \'O\'. 
  First person to get a row of their character wins.
  Rows can be Horizontally, Vectically, and Diagonally.
  Now let the game begin\n""")

def playerMove(game): # Your move will keep going till valid input
  valid = False
  print("YOUR MOVE".center(30,"~"))
  print(game)
  while valid == False:
    placement = input("\nWhere would you like to place your token >>> ")
    valid = game.place_token(placement,"X")
    if valid == False:
      print("Try Again")
  print("".center(30,"~"))

def comMove(game): # Computer move. This is random
  valid = False
  print("MY MOVE".center(30,"~"))  
  print(game)
  while valid == False:
    placement = random.randint(1,9)
    placement = str(placement)
    valid = game.place_token(placement,"O")
  print("".center(30,"~"))

def main(): #Main nuff said
  rules()
  game = TicTacToe()
  for turn in range(9):
    player = game.getTurn()
    if player == "X":
      playerMove(game)
    elif player == "O":
      comMove(game)

    if game.status == True:
      winner = game.is_winner()
      print(f"\nThe winner is: {winner}")
      print(game)
      break

  if game.status == False:
    print("Its a tie")
    print(game)

if __name__ == "__main__":
  main()