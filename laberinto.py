#Maze Runner
#Try to escape the maze following the empty spaces but whatch out... The maze can change the way out

#'E' is the entry
#'S' is the exit
#'X' are the walls
#' ' is the path

#You can't go through walls, neither diagonally
laberinto = [
    ['E', ' ', ' ', 'X', 'S'],
    ['X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', ' '],
    [' ', 'X', 'X', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

i = 0
j = 0
fin = False
while laberinto[i][j] != 'S' and fin != True:  

    if j+1 <5 and laberinto[i][j+1] == ' ':
        if laberinto[i][j+1] == 'S':
            fin = True
        else:
            print("Derecha ") 
            laberinto[i][j] = 'X'                 
            j = j+1
        
    elif i+1 <5 and laberinto[i+1][j] == ' ':
        if laberinto[i+1][j] == 'S':
            fin = True
        else:
            print("Abajo ")
            laberinto[i][j] = 'X'
            i = i+1
        
    elif j-1 >-1 and laberinto[i][j-1] == ' ':
        if laberinto[i][j-1] == 'S':
            fin = True
        else:
            print("izquierda ") 
            laberinto[i][j] = 'X'                   
            j = j-1
        
    elif i-1 >-1 and laberinto[i-1][j] == ' ':
        if laberinto[i-1][j] == 'S':
            fin = True
        else:
            print("arriba ") 
            laberinto[i][j] = 'X'                   
            i = i-1
    else:
        fin = True       
print()
