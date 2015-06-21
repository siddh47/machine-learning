from sklearn import linear_model
from numpy import dot
f,n = map(int,raw_input().strip().split())
x = []
y = []
for i in range(n):
    x.append([float(j) for j in raw_input().strip().split()])
    y.append(x[i].pop())
    print x[i]
# Initialize thetas, add bias term
classifier = linear_model.LinearRegression()
classifier.fit(x,y)
coefficients = [float(i) for i in classifier.coef_]

m = input()
for i in range(m):
    x = [float(j) for j in raw_input().strip().split()]
    print classifier.predict(x)[0]

