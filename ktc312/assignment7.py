import numpy as np
import matplotlib.pyplot as plt

# Question 1
def question1():
    x = np.arange(1,16).reshape(3,5).transpose(1,0)
    
    a = x[1::2]
    print "Answer 1-a:\n", a

    b = x[:,1]
    print "Answer 1-b:\n", b

    c = x[1:4,0:3]
    print "Answer 1-c:\n", c

    y=list()

    for element in a.flat:
        if element >11:
            pass
        elif element <3:
            pass
        else:
            y.append(element)
    d = np.asarray(y)
    print "Answer 1-d:\n", d

# Question 2
def question2():
    a = np.arange(25).reshape(5, 5)
    b = np.array([1., 5, 10, 15, 20])
    c = (a.transpose(1,0)*b).transpose(1,0)
    print "Answer 2:\n", c

# Question 3
def question3():
    a = np.random.rand(10, 3)
    b = np.argmin(abs(a - .5), axis=1).choose(a.T)
    print "Answer 3:\n", b

# Question 4
def question4():
    N_max = 50 
    some_threshold = 50
    
    x = np.linspace(-2, 1, 1000)
    y = np.linspace(-1.5, 1.5, 1000)
    c = x[:,np.newaxis] + 1j*y[np.newaxis,:]
    z=c

    for v in range(N_max):
        z = z**2 + c
    
    mask = (abs(z)<some_threshold)
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
    print 'ok'


if __name__ == "__main__":
    question1()
    question2()
    question3()
    question4()

