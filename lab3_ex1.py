import numpy as np
my_array1=np.zeros(shape=(4,3))
my_array2=np.zeros(shape=(4,3))
my_array3=np.zeros(shape=(4,3))
for (i,j),x in np.ndenumerate(my_array1):
    m = input(f'введите значение: строка {i}, столбец {j}: ')   
    my_array1[i,j]=float(m) 
for (i,j),x in np.ndenumerate(my_array2):
    n = input(f'введите значение: строка {i}, столбец {j}: ')   
    my_array2[i,j]=float(n) 
for (i,j),x in np.ndenumerate(my_array2):
    if my_array2[i,j]>my_array1[i,j] :
        my_array3[i,j]=my_array2[i,j]
    else :
        my_array3[i,j]=my_array1[i,j]
print(my_array3)