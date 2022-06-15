import threading
class FooBar():
    def __init__(self, n):
            self.n = n
    def foo(self):
        for _ in range(self.n):
            lockfoo.acquire()
            print("foo",end="")
            try:
                lockbar.release()
            except:
                pass
    def bar(self):
        for _ in range(self.n):
            lockbar.acquire()
            print("bar",end="")
            try:
                lockyeah.release()
            except:
                pass
    def yeah(self):
        for _ in range(self.n):
            lockyeah.acquire()
            print("yeah")
            try:
                lockfoo.release()
            except:
                pass
lockfoo=threading.Lock()
lockbar = threading.Lock()
lockyeah = threading.Lock()

if __name__=="__main__":
    obj=FooBar(int(input()))
    task=[threading.Thread(target=obj.foo),threading.Thread(target=obj.bar),threading.Thread(target=obj.yeah)]
    for t in task:
        t.start()
    for t in task:
        t.join()

