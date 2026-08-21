from threading import Thread
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello from thread!", i+1)
            sleep(0.3)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi from thread!", i+1)
            sleep(0.3)


if __name__ == "__main__":

    t1 = Hello()
    t2 = Hi()


    t1.start()
    t2.start()
    