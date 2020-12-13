import matplotlib.pyplot as plt
x=[0.1,99.99]
y=[5.45,385.38]
plt.plot(x,y,color='r',label='изменение массы монеты')
plt.xlabel('% от скорости света')
plt.ylabel('Масса монеты (грамм)')
plt.legend()
plt.grid()
plt.show()
