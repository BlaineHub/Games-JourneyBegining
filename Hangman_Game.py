def hangman(word):
  wrong = 0
  stages =  [" ",
             "__________           ",
             "         ¦           ",
             "         o            ",
             "        /¦\            ",
             "         ¦            ",
             "        / \            "
             ]

  rletters = list(word)
  board = ["_"]*len(word)
  win = False
  print("Welcome To Hangman")

  """wrong varaible is less then total stages game continues"""
  while wrong < len(stages)-1:
      print("\n")
      msg = "Guess A Letter? "
      char = input(msg)
      if char in rletters:
        cind = rletters.index(char)
        board[cind] = char
        rletters[cind] = "$"
        print(" ".join(board))
      else:
          wrong += 1
          """Joins board variable using a space"""
          print((" ".join(board)))
          e = wrong +1
          """Creates Hangman using new line"""
          print("\n".join(stages[0:e]))
      if "_"not in board:
         print("You Win! The Word Was:")
         print(" ".join(board))
         win = True
         break
  if not win:
      print("\n".join(stages[0:e]))
      print("you lose! it was {}.".format(word))

hangman("binx")