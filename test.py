import matplotlib.pyplot as plt
import numpy as np

def f1(t):
    return np.sin(2*np.pi*t)

def f2(t):
    return 1/t

def f3(t):
    return 2*t+3

t1=np.arange(0,5.1,0.02)
t2=np.arange(0.02,5.1,0.02)

plt.subplot(311)
plt.title('sine')
plt.ylim(-2,2)
plt.plot(t1,f1(t1),'k')

plt.subplot(312)
plt.title('1/x')
plt.grid(True)
plt.ylim(0,10)
plt.plot(t1,f2(t1),'r--')

plt.subplot(313)
plt.title('x')
plt.plot(t1,f3(t1),'g')

plt.subplots_adjust(hspace=0.5)
plt.show()
plt.close()
