# https://realpython.com/intro-to-python-threading/
# https://stackoverflow.com/questions/20886565/using-multiprocessing-process-with-a-maximum-number-of-simultaneous-processes
import logging
import threading
import concurrent.futures
from multiprocessing import Pool
import time
import random



def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


def thread_random_number(max_val):
    time.sleep(5)
    return max_val
    # return random.randint(0, max_val)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # ThreadPoolExecutor
    logging.info("Main    : before creating thread example 1")
    multithreaded_list = list()
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        t1 = executor.map(thread_random_number, range(100))
        multithreaded_list = list(t1)
    logging.info("Main    : after creating thread example 1")
    print(multithreaded_list)

    logging.info("Main    : before creating thread example 2")
    execution_list = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        t2 = executor.map(thread_random_number, execution_list)
        multithreaded_list = list(t2)
    logging.info("Main    : after creating thread example 2")
    print(multithreaded_list)

    # multiprocessing
    pool = Pool(processes=4)  # start 4 worker processes
    result = pool.apply_async(thread_random_number, [10])  # evaluate "f(10)" asynchronously
    # print(result.get(timeout=1))  # prints "100" unless your computer is *very* slow
    print(pool.map(thread_random_number, range(10)))  # prints "[0, 1, 4,..., 81]"