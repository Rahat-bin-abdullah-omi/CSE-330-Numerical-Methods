import numpy as np
import matplotlib.pyplot as plt

class Newtons_Divided_Differences:
    def __init__(self, differences, data_x):
        self.differences = differences
        self.data_x = data_x

    def __call__(self, x):
        """
        this function is for calculating y from given x using all the difference coefficients
        x can be a single value or a numpy
        the formula being used:
        f(x) = f [x0] + (x-x0) f[x0,x1] + (x-x0) (x-x1) f[x0,x1,x2] + . . . + (x-x0) (x-x1) . . . (x-xk-1) f[x0, x1, . . ., xk]

        work on this after implementing 'calc_div_diff'. Then you should have
        f[x0], f[x0,x1]. . . . . ., f[x0, x1, . . ., xk] stored in self.differences

        'res' variable must return all the results (corresponding y for x)
        """

        res = np.zeros(len(x)) #Initialization to avoid runtime error. You can change this line if you wish

        # place your code here!!!!!!!!!!!!!!!!!!!!!!!
        for i in range(len(res)):
            res[i] = self.newtonDiv(x[i])
        return res
    
    def newtonDiv(self, xi):
        res = 0
        for i in range(len(self.differences)):
            res += self.differences[i][0] * self.multiplier(xi, i)
        return res
    
    def multiplier(self, xi, i):
        res = 1
        for j in range(i):
            res *= xi - self.data_x[i]
        return res

#basic rule for calculating the difference, implanted in the lambda function. You may use it if you wish
difference = lambda y2, y1, x2, x1: (y2-y1)/(x2-x1)


def calc_div_diff(x,y):
    assert(len(x)==len(y))
    #write this function to calculate all the divided differences in the list 'b'
    b = [[] for i in range(len(x))]

    #place your code here!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in range(len(x)):
        for j in range(len(x)-i):
            if(i==0):
                b[i].append(y[j])
            else:
                b[i].append(difference(b[i-1][j+1],b[i-1][j],x[j+i],x[j]))
    return b


data_x = np.array([-3.,-2.,-1.,0.,1.,3.,4.])
data_y = np.array([-60.,-80.,6.,1.,45.,30.,16.])
# data_x = np.array([10.,15.,20.,22.5])
# data_y = np.array([227.4,362.78,517.35,602.97])
differences = calc_div_diff(list(data_x), list(data_y))
print(differences)
obj = Newtons_Divided_Differences(list(differences), list(data_x))

# #generating 50 points from -3 to 4 in order to create a smooth line
X = np.linspace(-3, 4, 50, endpoint=True)
F = obj(X)
plt.plot(X,F)
plt.plot(data_x, data_y, 'ro')
plt.show()