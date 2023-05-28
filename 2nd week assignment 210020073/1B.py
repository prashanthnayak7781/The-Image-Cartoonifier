import numpy as np

def compute_cost(years_experience, salary, w, b):
    m = len(years_experience)
    predicted_salary = w * years_experience + b
    cost = np.sum((predicted_salary - salary) ** 2) / (2 * m)
    return cost
w = 200
b = 100
years_experience = np.array([1, 3, 5])
salary = np.array([300, 480, 570])
cost = compute_cost(years_experience, salary, w, b)
print("Total cost:", cost)
