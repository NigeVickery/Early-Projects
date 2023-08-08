import math 
import numpy as np 
import matplotlib.pyplot as plt

# Calculate mean of x and y
def mean_X(x):
    return np.mean(x)

def mean_Y(y):
    return np.mean(y)

# Calculate slope (b1)
def slope(x, y, mean_x, mean_y):
    numerator = 0
    denominator = 0
    for i in range(len(x)):
        numerator += (x[i] - mean_x) * (y[i] - mean_y)
        denominator += (x[i] - mean_x) ** 2
    return numerator / denominator

# Calculate intercept (b0)
def intercept(mean_x, mean_y, b1):
    return mean_y - (b1 * mean_x)

# Generate regression line points
def regression_line_points(x, b0, b1):
    reg_line_x = [min(x), max(x)]
    reg_line_y = [b0 + b1 * min(x), b0 + b1 * max(x)]

def plot_regression_line(x, y, b0, b1):
    plt.scatter(x, y, color='m', marker='o', s=30)
    y_pred = b0 + b1 * x
    plt.plot(x, y_pred, color='g')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Calculate correlation coefficient
def correlation_coefficient(x, y, mean_x, mean_y):
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    denominator_x = sum((x[i] - mean_x) ** 2 for i in range(len(x)))
    denominator_y = sum((y[i] - mean_y) ** 2 for i in range(len(y)))
    R = (numerator / math.sqrt(denominator_x * denominator_y))
    return R

def main():
    DATASIZE = int(input('Enter the number of data points: '))
    DEGREE = int(input('Enter the degree of the polynomial: '))
    X_COEFFICIENT = int(input('Enter the coefficient of x: '))

    if DATASIZE <= 0: 
        print('Invalid data size\n') 
        return 
    elif DEGREE <= 0: 
        print('Invalid degree - must be positive\n') 
        return
    # Generate random points
    x = np.random.randint(1, 30, size=DATASIZE)
    y = X_COEFFICIENT * x**DEGREE + np.random.randint(1, 30, size=DATASIZE)

    mean_x = mean_X(x)
    mean_y = mean_Y(y)

    b1 = slope(x, y, mean_x, mean_y)
    b0 = intercept(mean_x, mean_y, b1)

    # Print y = b0 + b1 * x`with 2 decimal places
    print(f'y = {b0:.2f} + {b1:.2f}x')
    # Print correlation coefficient with 2 decimal places
    print(f'Correlation coefficient: R = {correlation_coefficient(x, y, mean_x, mean_y):.2f}')

    plot_regression_line(x, y, b0, b1)


if __name__ == '__main__':
    main()

