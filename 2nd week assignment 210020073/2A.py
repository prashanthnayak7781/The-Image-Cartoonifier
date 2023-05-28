import numpy as np

def compute_gradient_descent(x_train, y_train, w_init, b_init, alpha, num_iters):
    w = w_init
    b = b_init
    
    for i in range(num_iters):
        cost = compute_cost(x_train, y_train, w, b)
        dw, db = compute_gradient(x_train, y_train, w, b)
        
        w -= alpha * dw
        b -= alpha * db
    
    return w, b

w_init = 0
b_init = 0
alpha = 0.01
num_iters = 10000

x_train = np.array([1, 3, 5])
y_train = np.array([300, 480, 570])

w_final, b_final = compute_gradient_descent(x_train, y_train, w_init, b_init, alpha, num_iters)

print("Final value of w:", w_final)
print("Final value of b:", b_final)
