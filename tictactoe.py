#stage 2
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

while True:
  p1turn()
  p2turn()
