import random
import copy


def userinputs():

    print("<-----------------------------------------------------------------WELCOME! LET'S PLAY A GAME----------------------------------------------------------------------------------->")
    print("ENTER THE NO OF COLUMNs. MAXIMUM SIZE OF ROWS IS 12 AND MINIMUM IS 4:",end=" ")

#TAKING NO OF COLUMN AS INPUT
    XSIZE = int(input())
    print("ENTER THE NO OF ROWS. MAXIMUM SIZE OF ROWS IS 14 AND MINIMUM IS 6:",end=" ")

##TAKING NO OF ROWS AS INPUT
    YSIZE = int(input())

#NO OF FAKE TICKETS
    NUMOFFAKES = 25

# NO OF CHANCES FOR THE USER
    NUMATTEMPTS = 30
    result = [XSIZE,YSIZE,NUMOFFAKES,NUMATTEMPTS]
    return result


if __name__ == '__main__':
    a=userinputs()
    numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']
    alphabets = list('ABCDEFGHIJKLMN')
    b = numbers[0:a[1]+1]
    c = alphabets[0:a[0]]
    c.insert(0,' ')
    if 4<=a[0]<=12 and 6<=a[1]<=14:
        board = []
        for i in range(a[1]):
            row = []
            for j in range(a[0]):
                row.append(' ')
            board.append(row)

# RANDOMLY GENERATING THE FAKE TICKETS
        count = 0
        faketcketboard= copy.deepcopy(board)
        while count < a[2]:
            x = random.randint(0, a[0] - 1)
            y = random.randint(0, a[1]- 1)
            if faketcketboard[y][x] != 'FT':
                faketcketboard[y][x] = 'FT'
                count += 1

#PRINTING WHERE ALL THE FAKE TICKETS ARE
        No_Of_Remaining_Moves = 30
        score = 0
        l=[]
        while(No_Of_Remaining_Moves>0):

#ASKING FOR INPUT OF THE TICKET LOCATION
                  print("PLEASE ENTER THE LOCATION TO FIND THE FAKE TICKET:")

#PRINTIG ALL THE SEATS AFTER THE SELECTION
                  print('Section of Seats')
                  print('  '.join(c))
                  for i, row in enumerate(board):
                      print(str(i + 1) + '  '+ '  '.join(row))

#TAKING INPUT OF THE LOCATION
                  user_input = input('Enter a seat coordinate: ')
                  if user_input in l or user_input[0].upper() not in c or user_input[1:] not in b:
                      print("Invaild seat .Enter a valid seat coordinate")
                      print("THE NO OF MOVES REMAINING ARE {}".format(No_Of_Remaining_Moves))
                      print("THE CURRENT SCORE IS {}".format(score))
                      continue
                  else:
                      l.append(user_input)

#CHECKING WHETHER THE LOCATION IS VALID OR NOT
                  while 2<len(user_input)>3 or user_input[1:] not in b or user_input[0].upper() not in c:
                      user_input = input('Invalid input. Enter a seat coordinate: ')
                  x = 'ABCDEFGHIJKLMN'.index(user_input[0].upper())
                  y = int(user_input[1]) - 1
                  No_Of_Remaining_Moves -= 1
                  if faketcketboard[y][x] == 'FT':
                      board[y][x] = 'X'
                      score += 1
                  else:
                      board[y][x] = 'O'

#PRINTING NO OF REMAINING MOVES
                  print("THE NO OF MOVES REMAINING ARE {}".format( No_Of_Remaining_Moves))

#PRINTING THE CURRENT SCORE
                  print("THE CURRENT SCORE IS {}".format(score))

# CHECKING IF THE GAME IS OVER
                  if score >= (a[2] * 2) / 3:
                      print('YOU WON! YOU GUESSED {} FAKE TICKETS!'.format(score))
                      break

#GAME OVER IF NUMBER OF MOVES ARE FINISHED
        if No_Of_Remaining_Moves == 0:
            print('YOU LOST! YOU ONLY FOUND {} FAKE TICKETS!'.format(score))

#PRINTING IF THE USER GAVE WRONG ROWS AND COLUMNS
    else:
        print("PLEASE ENTER VALID NUMBER OF ROWS AND COLUMNS")
        userinputs()



7