import matplotlib.pyplot as plt
x=[0.1,99.99]
y=[5.45,385.38]
plt.plot(x,y,color='r',label='изменение массы монеты',ms=5)
plt.xlabel('% от скорости света')
plt.ylabel('Масса монеты')
plt.legend()
plt.grid()
plt.show()
