from multiprocessing import Process,Queue
def f1(q):
    q.put("字符串")

def f2(q1,q2):
    a = q1.get()
    print(a)
    q2.put(a)

def f3(q2):
    a = q2.get()
    print(a)

if __name__ == "__main__":
    q1 = Queue()
    q2 = Queue()
    p1 = Process(target=f1,args=(q1,))
    p2 = Process(target=f2,args=(q1,q2))
    p3 = Process(target=f3,args=(q2,))
    p1.start()
    p1.join()
    p2.start()
    p3.start()
    p2.join()
    p3.join()