##**m = tanh((h+z*m)/T)**


import numpy as np
import matplotlib.pyplot as plt
import itertools
plt.rcParams["figure.figsize"] = [10, 5]
plt.rcParams["figure.autolayout"] = True
def g(m, T, h, z):
  return (m - np.tanh((h+z*m)/T))

#tim nghiem cua phuong trinh g(m, T) = 0 bang phuong phap bisection
#T : nhiet do
#m1, m2: khoang chua nghiem
def find_m(T, m1, m2, h, z):
  epsilon = 1e-10
  if (g(m1, T, h, z) * g(m2, T, h, z)) >0:
    return 0
  while((m2 - m1) >= epsilon):
    mid = (m1 + m2) / 2
    if (g(m1, T, h, z)*g(mid, T, h, z)) < 0:
      m2 = mid
    if (g(m2, T, h, z)*g(mid, T, h, z)) < 0:
      m1 = mid
  return mid

#Tlist chua cac gia tri T trong khoang can tinh
#mlist chua cac nghiem cua g(m, T) = 0 voi T tuong ung

h = 0
zlist = [2, 4, 6, 12]
Tlist = np.linspace(0.001, 16, 10000)
#ve do thi m phu thuoc vao T voi z thay doi
style = itertools.cycle(['o', 'v', '^', 's', 'p', '*', 'D', 'P', 'X'])

for z in zlist:
  mlist = []
  for _ in Tlist:
    mlist.append(find_m(_, 0.001, 1.00001, h, z))
  plt.plot(Tlist, mlist, label=f"h={h}, z={z}", marker=next(style), markevery=slice(500, 6000, 500))

plt.xlabel("T", fontsize="xx-large", fontweight="bold")
plt.ylabel("m", fontsize="xx-large", fontweight="bold")
plt.text(7.5, 0.4, "FM", fontsize="xx-large", fontweight="bold")
plt.text(14, 0.4, "PM", fontsize="xx-large", fontweight="bold")
plt.xticks(np.arange(min(Tlist), max(Tlist)+1, 2))#chia độ chia cho trục x
plt.yticks(np.arange(0, 1.1, 0.2))
plt.legend(fontsize=20)
plt.show()



#Tlist chua cac gia tri T trong khoang can tinh
#mlist chua cac nghiem cua g(m, T) = 0 voi T tuong ung

style = itertools.cycle(['o', 'v', '^', 's', 'p', '*', 'D', 'P', 'X'])
hlist = [0, 0.2, 0.4, 0.8, 1]
z = 6
array = np.linspace(0.001, 18, 10000)
#ve do thi m phu thuoc vao T voi z co dinh, h thay doi
for h in hlist:
  Tlist = []
  mlist = []
  for _ in array:
    Tlist.append(_)
    mlist.append(find_m(_, 0.001, 1.00001, h, z))
  plt.plot(Tlist, mlist, label=f"z = {z}, h = {h}", marker=next(style), markevery=slice(4000, 7000, 1200))

plt.xlabel("T", fontsize="large", fontweight="bold")
plt.ylabel("m", fontsize="large", fontweight="bold")
plt.xticks(np.arange(min(Tlist), max(Tlist)+1, 2))
plt.legend()
plt.show()

#define g(m) = m - tanh((h+m*z)/T)
import numpy as np
def g(m, T, h, z):
  return (m - np.tanh((h+z*m)/T))

#tim nghiem cua phuong trinh g(m, h) = 0 bang phuong phap bisection
#T : nhiet do
#m1, m2: khoang chua nghiem
#z: so lan can gan nhat
#h:
def find_m(T, m1, m2, h, z):
  epsilon = 1e-10
  if (g(m1, T, h, z) * g(m2, T, h, z)) >=0:
    return 0
  while((m2 - m1) >= epsilon):
    mid = (m1 + m2) / 2
    if (g(m1, T, h, z)*g(mid, T, h, z)) < 0:
      m2 = mid
    if (g(m2, T, h, z)*g(mid, T, h, z)) < 0:
      m1 = mid
  return mid

import numpy as np
from matplotlib import pyplot as plt
import itertools
def plot(a, b, T, z, style):
  plt.plot(a, b, label=f"T = {T} z = {z}", marker=next(style), markevery=50)
  plt.legend(loc=4, fontsize = 12)

style = itertools.cycle(['o', 'v', '^', 's', 'p', '*', 'D', 'P', 'X'])

mlist = []
m1 = 0.001
m2 = 1.0001
T = np.array([4.5, 5, 5.5, 6, 7, 8, 9, 10, 11, 12])
z = 6
hlist = np.arange(0, 2, 0.01)
#plt.figure(figsize=[12, 6])
for t in T:
  mlist = []
  for _ in hlist:
    mlist.append(find_m(t, m1, m2, _, z))
  plot(hlist, mlist, t, z, style)
plt.xlabel("h", fontsize="xx-large", fontweight="bold")
plt.xticks(np.arange(min(hlist), max(hlist)+1, 0.2))
plt.yticks(np.arange(0, 1+0.1, 0.2))
plt.ylabel("m", fontsize="x-large", fontweight="bold")
