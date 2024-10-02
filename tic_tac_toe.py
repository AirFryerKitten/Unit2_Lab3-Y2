import random 

class TicTacToe:
  def __init__(self):
    self.__board = [[str(x+(3*y)+1) for x in range(3)] for y in range(3)]
    self.__turn = random.choice(["X","O"])
    self.status = False

  # __board looks like this 
  # 1 2 3
  # 4 5 6 
  # 7 8 9 

  def __str__(self): #Prints the board
    currentBoard = "-----------\n"
    for row in self.__board:
      currentBoard += f" {row[0]} | {row[1]} | {row[2]}\n"
      currentBoard += "-----------\n"
    return currentBoard
  
  def getTurn(self):# This is to get the current player
    return self.__turn
  
  def is_winner(self): # Check to see who the winner is 
    return self.__turn

  def __check_win(self): # checks if anyone has won

    for num in range(len(self.__board)):

      if self.__board[num][0] == self.__board[num][1] == self.__board[num][2]:
        self.status = True

      elif self.__board[0][num] == self.__board[1][num] == self.__board[2][num]:
        self.status = True
      
      elif self.__board[0][0] == self.__board[1][1] == self.__board[2][2]:
        self.status = True

      elif self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
        self.status = True

      else:
        if self.__turn == "X":
          self.__turn = "O"
        elif self.__turn == "O":
          self.__turn = "X"


  def place_token(self,placement, token): #Checks if you can place in that spot then places
    if placement == "1":
      if self.__board[0][0] == "1":
        self.__board[0][0] = token
        self.__check_win()
        return True

      else:
        return False
    
    elif placement == "2":
      if self.__board[0][1] == "2":
        self.__board[0][1] = token
        self.__check_win()
        return True

      else:
        return False

    elif placement == "3":
      if self.__board[0][2] == "3":
        self.__board[0][2] = token
        self.__check_win()
        return True

      else:
        return False

    elif placement == "4":
      if self.__board[1][0] == "4":
        self.__board[1][0] = token
        self.__check_win()
        return True

      else:
        return False

    elif placement == "5":
      if self.__board[1][1] == "5":
        self.__board[1][1] = token
        self.__check_win()
        return True

      else:
        return False

    elif placement == "6":
      if self.__board[1][2] == "6":
        self.__board[1][2] = token
        self.__check_win()
        return True

      else:
        return False

    elif placement == "7":
      if self.__board[2][0] == "7":
        self.__board[2][0] = token
        self.__check_win()
        return True

      else:
        return False

    elif placement == "8":
      if self.__board[2][1] == "8":
        self.__board[2][1] = token
        self.__check_win()
        return True

      else:
        return False

    elif placement == "9":
      if self.__board[2][2] == "9":
        self.__board[2][2] = token
        self.__check_win()
        return True

      else:
        return False
  
