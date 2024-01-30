def formingMagicSquare(s=None):
    # make magic square
    magic_square = []
    one_location = [[0, 1], [1, 0], [1, 2], [2, 1]]
    
    for one in one_location:
        x, y = one[0], one[1]

        temp = [[0, 0, 0], [0, 5, 0], [0, 0, 0]]
        temp[x][y] = 1
        
        for i in range(2, 10):
            if i == 5: continue
            if x - 1 < 0:
                x = 2
            else:
                x -= 1
            
            if y + 1 >= 3:
                y = 0
            else:
                y += 1
            
            if temp[x][y] == 0:
                temp[x][y] = i
            else:
                x += 1
                y -= 2
                
                if x < 0 and y == 3:
                    x = 0
                    y = 1
                    
                    temp[x][y] = i
                else:
                    temp[x][y] = i
        print(temp)
        break

if __name__ == "__main__":
    formingMagicSquare()