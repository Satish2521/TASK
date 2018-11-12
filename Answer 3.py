
# Use Multithreading we inprove the time..and will Excute this program much faster


import time
import threading
x=[2,3,8,9]  
def square(numbers):
    print("Calculate Square Numbers")
    for p in numbers:
        time.sleep(0.2)
        print('square:', p*p)
def cube(numbers):
    print("Calculate cube Numbers")
    for p in numbers:
        time.sleep(0.2)
        print('cube:',p*p*p)

t = time.time()
t1 = threading.Thread(target = square, args = (x,))
t2 = threading.Thread(target = cube, args = (x,))
t1.start()
t2.start()
t1.join()
t2.join()
print("done in :",time.time()-t)
