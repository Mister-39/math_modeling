import matplotlib.pyplot as plt
x=[0,99.99]
y=[0,4.14]
plt.plot(x,y,color='r',label='изменение кинетической энргии монеты')
plt.xlabel('% от скорости света')
plt.ylabel('Кинетичекая энергия монеты (МегаТонн)')
plt.legend()
plt.grid()
plt.show()

