#seating = [[l[0:7],l[7:10]] for l in open('day-5-input.txt','r')]
seating = [['FBFBBFF','LLR']]

for board in seating:
    print(board)
    rows = [0,127]
    columns = [0,8]
    for r in board[0]:
        #print('board[0] is ',board[0])
        if r == 'F':
            rows[1] = rows[1] - int((rows[1] - rows[0])/2)
            #print('upper limit is now ', rows[1])
            print(rows)
        else:
            rows[0] = rows[0] + int((rows[1] - rows[0])/2)
            #print('lower limit is now', rows[0])
            print(rows)
    if board[0][-1] == 'F':
        print('seat is in row',rows[0])

#print(seating)