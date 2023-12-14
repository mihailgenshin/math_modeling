import matplotlib.pyplot as plt
import numpy as np

def hyperbole_plotter(a=8):

    x = np.arange(-10, 10)
    y = a/x

    plt.plot(x, y, label='my hyperbole')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('hyperbole')
    plt.legend()
    
    plt.savefig('fig_6.png')


if __name__ == '__main__':
	hyperbole_plotter()