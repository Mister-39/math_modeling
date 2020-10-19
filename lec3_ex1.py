import numpy as np
my_array=np.zeros(shape=(4,3))
for (i,j),x in np.ndenumerate(my_array):
    m = input(f'введите значение: строка {i}, столбец {j}: ')   
    my_array[i,j]=float(m) 
    print(i,j,x,sep=';')
    
print(my_array)