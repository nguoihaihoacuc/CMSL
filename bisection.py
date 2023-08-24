##**m = tanh(mT)**

#define g(m) = m - tanh(mT)
import numpy as np
def g(m, T):
  return m - np.tanh(m*T)


#ve do thi
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 4.50]
plt.rcParams["figure.autolayout"] = True

x = np.linspace(0, 2, 100)
I = np.linspace(0, 1, 10)
y = np.zeros(1000)

plt.plot(x, g(x, 20), color="red")
plt.plot(x, y, linestyle="dashed")
plt.xlabel("m")
plt.ylabel("m - tanh(mT)")
plt.show()




x1 = float(input("enter x1"))
x2 = float(input("enter x2"))

error = 0.00001
temp = (x2 + x1) / 2
dx = abs(x2 - x1)
for i in I:
if (g(x1, 20)*g(x2, 20) > 0):
  print("no root")
elif g(temp, 20) == 0:
  print("root = ", temp)
else:
  while(dx >= error):
    if (g(x1, 20)*g(temp, 20)) < 0:
      x2 = temp
      temp = (x2 + x1) / 2
    elif (g(x2, 20)*g(temp, 20)) < 0:
      x1 = temp
      temp = (x2 + x1) / 2
    dx = abs(x2 -x1)
  print("root = ", temp)



