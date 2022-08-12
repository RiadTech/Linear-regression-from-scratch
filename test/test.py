import matplotlib.pyplot as plt
from src.main import *
import pandas as pd
data = pd.read_csv("Your csv file")
m = 0
b = 0
L = 0.0001
epochs = 1000

for i in range(epochs):
    if i % 50 == 0:
        print("Epoch: {i}")

    
    m, b = gradient_descent(m, b)

print(m, b)

plt.scatter(data.studytime, data.score, color="red")
plt.plot(list(range(20, 80)), (m *x + b for x in range(20, 80)), color="black")
plt.show()
