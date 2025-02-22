import numpy as np

# def gradient_descent(x,y):
#     m_curr = b_curr = 0
#     iterations = 1000
#     n = len(x)
#     learning_rate = 0.01

#     for i in range(iterations):
#         y_predicted = m_curr * x + b_curr
#         md = -(2/n) * sum (x * (y_predicted - y))
#         cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
#         bd = -(2/n) * sum (y_predicted - y)
#         m_curr = m_curr - learning_rate * md
#         b_curr = b_curr - learning_rate * bd
#         print("m: {}, b: {}, cost: {} iteration: {}".format(m_curr,b_curr,cost,i))






# x = np.array([1,2,3,4])
# y = np.array([5,7,9,11])

# gradient_descent(x,y)
