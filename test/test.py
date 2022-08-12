from src.main import *
import matplotlib.pyplot as plt
import pandas as pd
m = 0
b = 0
L = 0.0001
epochs = 1000

for i in range(epochs):
    m, b = gradient_descent(m, b)