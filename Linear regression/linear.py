import numpy as np
import pandas as py
import matplotlib.pyplot as plt

def estimate_coef(x, y):
	n = np.size(x)
	m_x, m_y = np.mean(x), np.mean(y)
	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x
	# calculating regression coefficients
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x
	return(b_0, b_1)

def plot_regression_line(x, y, b):
	# plotting the actual points as scatter plot
	plt.scatter(x, y, color = "m",
			marker = "o", s = 30)

	y_pred = b[0] + b[1]*x
	plt.plot(x, y_pred, color = "g")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()

def main():

    data = py.read_csv("linear.csv")
    x = data['x']
    y = data['y']

    b = estimate_coef(x,y)
    print("Estimated coefficients:\nb_0 = {} \
	\nb_1 = {}".format(b[0], b[1]))
    plot_regression_line(x,y,b)

if __name__ == "__main__":
	main()
