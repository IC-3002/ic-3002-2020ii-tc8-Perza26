def contar_rutas_mas_cortas(C):
    f= len(C)
    c= len(C[0])
    Rs= [[0 for x in range(c)] for y in range(f)]
    for i in range(f):
        for j in range(c):
            if Rs[i][j] == 0:
                if  i==0 or j==0:
                    Rs[i][j]=1
                elif C[i][j]==0 and i>0 and j>0:
                    Rs[i][j]=Rs[i-1][j]+Rs[i][j-1]
    return Rs[i][j]