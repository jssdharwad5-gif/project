import multiprocessing
def A(a,b):
    return a+b
def B(a,b):
    return a-b
def C(a,b):
    return a*b
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=A, args=(5, 3))
    p2 = multiprocessing.Process(target=B, args=(5, 3))
    p3 = multiprocessing.Process(target=C, args=(5, 3))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("All functions have completed.")
