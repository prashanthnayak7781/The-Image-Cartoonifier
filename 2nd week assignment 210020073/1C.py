import numpy as np

def compute_gradient(years_experience, salary, w, b):
    m = len(years_experience)
    predicted_salary = w * years_experience + b
    dw = np.sum((predicted_salary - salary) * years_experience) / m
    db = np.sum(predicted_salary - salary) / m
    
    return dw, db
w = 200
b = 100
years_experience = np.array([1, 3, 5])
salary = np.array([300, 480, 570])
dw, db = compute_gradient(years_experience, salary, w, b)

print("Derivative of J w.r.t w:", dw)
print("Derivative of J w.r.t b:", db)
