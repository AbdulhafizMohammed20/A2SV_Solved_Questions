matrix = []
move = 0
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)


for r in range(5):
    for col in range(5):

        if matrix[r][col] == 1:
            move = abs(2-r )+ abs(2 - col)
            break
    
            
    

print(move)
