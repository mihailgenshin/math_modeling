import matplotlib.pyplot as plt 

x=[1, 1, 5, 5]
y=[1, 5, 5, 1]

plt.plot(x, y, color='b',label='Graf 1', marker='>', ms=5)
plt.plot(y, x, color='b',label='Graf 2', marker='o', ms=3)
plt.axis('equal')

plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.title('Base')

plt.savefig('fig_5.png')