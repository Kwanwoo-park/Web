import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'bx-', label='First function')
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro--', label='Second function')

plt.xlabel('X')
plt.ylabel('Y')

plt.title('matplotlib sample')
plt.legend(loc='best')

plt.xlim(0, 6)
plt.savefig('advanced_graph.png', dpi=300)
plt.show()