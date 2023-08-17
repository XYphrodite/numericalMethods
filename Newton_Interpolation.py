import numpy as np
import matplotlib.pyplot as plt

def GetAArr():
    for i in range(startN):
        a_arr.append(GetA(x_arr, y_arr,a_arr))
    return a_arr

def GetA(x_arr,y_arr,a_arr):
    n = len(a_arr)
    a = (y_arr[n]-(GetASum(x_arr[n],a_arr)))/(GetXPolynom(x_arr[n],n)) 
    return a 


def GetASum(x,a_arr):
    sum = 0
    for i in range(len(a_arr)):
        sum += a_arr[i]*GetXPolynom(x,i)
    return sum


def GetXPolynom(x, num):
    x_p = 1
    for i in range(num):
        x_p *= (x-x_arr[i])
    return x_p


x_arr = [1,2,4,7]
y_arr = [2,3,1,4]

startN = len(x_arr)
x__to_inter_arr = np.linspace(min(x_arr), max(x_arr), 100)
a_arr = []
GetAArr()

def Interpolize(x_arr_inter):
    y_arr_inter = []
    for i in x_arr_inter:
        y_arr_inter.append(GetASum(i,a_arr))
    return y_arr_inter


fig, ax = plt.subplots()
ax.plot(x_arr, y_arr)
ax.plot(x__to_inter_arr, Interpolize(x__to_inter_arr))

ax.grid()

plt.show();