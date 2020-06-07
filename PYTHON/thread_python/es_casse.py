import threading
import logging
import random


def cassa():
    totB=100
    numB=[0,1,2,3,4,5,6,7,8,9,10]

    tiket = (int)(1+ random.choice(numB))
    print(totB)

    if totB==0:     #tiket esauriti
        print("tiket esauriti")

    elif totB>0 and tiket<=totB:
         print(f"tiket acquistati {tiket}" )
         totB=totB-tiket

    elif 0 < totB < tiket:
         print("tiket acquistati = " + totB)
         totB=0

    s.release()

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads=[]

    for _ in range(1,10):
        threads.append(threading.Thread(format=cassa()))

    s = threading.Lock()
    
    s.acquire()
    
    for i in range(0,9):
        threads[i].start()

    for i in range(0,9):
        threads[i].join()