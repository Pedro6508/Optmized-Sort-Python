def Max( arr = [] ): #Menor elemento de um array de 2 elementos
    if( arr[0] >= arr[1] ):
        return arr[0]
    else:
        return arr[1]

def Min( arr = [] ): #Maior elemento de um array de 2 elementos
    if( arr[0] <= arr[1] ):
        return arr[0]
    else:
        return arr[1]

def MaxOrMinElementArray( begin, end, MinOrMax, array = [] ):
    if( end - begin <= 1 ):
        MaxValue = MinOrMax( [ array[begin],array[end] ] )
        if( MaxValue == array[begin] ):
            return [ MaxValue, begin ]
        else:
            return [ MaxValue, end ]
    else:
        Mindex = ( begin + end )//2 # Mindex = Middle + index 
        return MinOrMax( [ MaxOrMinElementArray( begin     , Mindex, MinOrMax, array ),
                           MaxOrMinElementArray( Mindex + 1, end   , MinOrMax, array ) ] )

lista = [100,100,2,13,45,50,160,7,98,9] 
listaSize = 10 
listaLastIndex = listaSize - 1
neutralElement = MaxOrMinElementArray( 0, listaLastIndex, Min, lista )[0] - 1 
sortedLista = [100,100,2,13,45,50,160,7,98,9] 

print( "Esta é a lista inicial:  ", lista ) 

for i in range( 0, listaSize ):
    MaxEl = MaxOrMinElementArray( 0, listaLastIndex, Max, lista )
    sortedLista[i] = MaxEl[0] 
    lista[ MaxEl[1] ] = neutralElement

print( "Lista final: ", sortedLista )



