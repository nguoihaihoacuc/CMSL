#define g(m) = m - tanh(mT)
import numpy as np
z=4
def g(m, T):
  return (m - np.tanh(z*m/T))

#define bisection function
def bisection(T, m1, m2, Tlist, mlist):
  epsilon = 1e-10
  if (g(m1, T) * g(m2, T)) >0:
    print("no root")
    return
  while((m2 - m1) >= epsilon):
    mid = (m1 + m2) / 2
    if (g(m1, T)*g(mid, T)) < 0:
      m2 = mid
    if (g(m2, T)*g(mid, T)) < 0:
      m1 = mid
  Tlist.append(T)
  mlist.append(mid)

#use bisection function with T in (0.001, 4)
Tlist = []
mlist = []
T = np.linspace(0.001, 4, 10000)
for i in T:
  bisection(i, 0.001, 1.00001, Tlist, mlist)

#draw m depends on T
plt.plot(Tlist, mlist)
plt.xlabel("T")
plt.ylabel("m")
plt.show()
