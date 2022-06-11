import time
from random import randint


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        results = func(*args, **kwargs)
        t = time.time() - start
        if t>60*2:
            t = f"{func.__name__!r} >> Executed in {round(t/60,2)}min."
        else:
            t = f"{func.__name__!r} >> Executed in {int(round(t,0))}sec."
        print(t)
        return results
    return wrapper



def dummy_func(i,j):
    r = i**j
    time.sleep(2)
    return r


def dummy_worker(*args, **kwargs):
    if "fail" in kwargs.keys():
        if kwargs["fail"]==True:
            i = randint(0,10)
        else:
            i = randint(1,10)
    else:
        i = randint(1,10)
    if i==0:
        e = f"Dummy Error, value is {i}"
        raise Exception(e)
    else:
        time.sleep(1.5)
    try:
        return {"a": args[0], "i": i, "i2": args[0]+i}
    except:
        return {"i": i, "i2": args[0]+i}


 
def dummy_worker_error(*args, **kwargs):
    i = randint(0,10)
    if i in (0,3,5):
        e = f"Dummy Error, value is {i}"
        raise Exception(e)
    else:
        time.sleep(1.5)
    try:
        return {"a": args[0], "i": i, "i2": args[0]+i}
    except:
        return {"i": i, "i2": args[0]+i}



def dummy_worker_int_str(arg1:int, arg2:str):
    i = randint(0,10)
    if i in (0,3,5):
        e = f"Dummy Error, value is {i}"
        raise Exception(e)
    else:
        time.sleep(i)
    response = {"i": i, "arg1": arg1, "arg2": arg2}
    print(response)
    return response