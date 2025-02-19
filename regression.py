import numpy as np
import matplotlib.pyplot as plt

x_input = list(map(int, input("Enter x values: ").split()))
y_input = list(map(int, input("Enter y values: ").split()))
# Sample data
X = np.array(x_input)
y = np.array(y_input)

# Calculate the coefficients
def linear_regression(X, y):
    X_mean = np.mean(X)
    y_mean = np.mean(y)
    numerator = np.sum((X - X_mean) * (y - y_mean))
    denominator = np.sum((X - X_mean) ** 2)
    slope = numerator / denominator
    intercept = y_mean - slope * X_mean
    return slope, intercept
def correlation_coefficient(X, y):
    X_mean = np.mean(X)
    y_mean = np.mean(y)
    numerator = np.sum((X - X_mean) * (y - y_mean))
    denominator = np.sqrt(np.sum((X - X_mean) ** 2) * np.sum((y - y_mean) ** 2))
    return numerator / denominator

slope, intercept = linear_regression(X, y)
# Predict values
y_pred = slope * X + intercept
correlation_coefficient = correlation_coefficient(X, y)

# Print the coefficients
print(f'Coefficient: {slope}')
print(f'Intercept: {intercept}')
print(f'Correlation coefficient: {correlation_coefficient}')

# Plot the results using matplotlib
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', label='Fitted line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()
