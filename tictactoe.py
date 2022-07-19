#stage 3
line0 = ["-", "-", "-"]
line1 = ["-", "-", "-"]
line2 = ["-", "-", "-"]
def display():
  print("\n Printing board...", "\n", line0, "\n", line1, "\n", line2, "\n")
display()

def p1turn():
  check=9
  while check != 0:
    print("Player 1, make your move")
    x = int(input("Enter row # (0-2): "))
    y = int(input("Enter column # (0-2): "))

    if y == 0:
      if line0[x] == "-":
        line0[x] = "X"
        check=0
      else:
        check=2
    elif y == 1:
      if line1[x] == "-":
        line1[x] = "X"
        check=0
      else:
        check=2
    elif y == 2:
      if line2[x] == "-":
        line2[x] = "X"
        check=0
      else:
        check=2
    else:
      check=1
    if check == 2:
      print(f"***BOARD[{x}] [{y}] HAS BEEN SELECTED ALREADY***")
      print("**PLEASE SELECT AGAIN**")
    elif check == 1:
      print("***INVALID ROW OR COLUMN***")
      print("**PLEASE SELECT AGAIN**")

  display()

def p2turn():
  check=9
  while check != 0:
    print("Player 2, make your move")
    x = int(input("Enter row # (0-2): "))
    y = int(input("Enter column # (0-2): "))

    if y == 0:
      if line0[x] == "-":
        line0[x] = "O"
        check=0
      else:
        check=2
    elif y == 1:
      if line1[x] == "-":
        line1[x] = "O"
        check=0
      else:
        check=2
    elif y == 2:
      if line2[x] == "-":
        line2[x] = "O"
        check=0
      else:
        check=2
    else:
      check=1
    if check == 2:
      print(f"***BOARD[{x}] [{y}] HAS BEEN SELECTED ALREADY***")
      print("**PLEASE SELECT AGAIN**")
    elif check == 1:
      print("***INVALID ROW OR COLUMN***")
      print("**PLEASE SELECT AGAIN**")

  display()


def win():
  if line0[0]+line0[1]+line0[2]==("XXX"or"OOO"):
    return True
  elif line1[0]+line1[1]+line1[2]==("XXX"or"OOO"):
    return True
  elif line2[0]+line2[1]+line2[2]==("XXX"or"OOO"):
    return True
  elif line0[0]+line1[0]+line2[0]==("XXX"or"OOO"):
    return True
  elif line0[1]+line1[1]+line2[1]==("XXX"or"OOO"):
    return True
  elif line0[2]+line1[2]+line2[2]==("XXX"or"OOO"):
    return True
  elif line0[0]+line1[1]+line2[2]==("XXX"or"OOO"):
    return True
  elif line0[2]+line1[1]+line2[0]==("XXX"or"OOO"):
    return True
  else:
    return False

for x in range(4):
  p1turn()
  if win()==True:
    print("Player 1 wins")
    break
  p2turn()
  if win()==True:
    print("Player 2 wins")
    break
p1turn()
if win()==True:
  print("Player 1 wins")
else:
  print("Its a tie")