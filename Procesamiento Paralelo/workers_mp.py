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
    """
        args = positional arguments
        kwargs = named arguments
    """
    ## debugging
    try:
        debug = kwargs["debug"]
    except:
        debug = False
    if debug==True: print("*"*50, " Start debugging.")
    ## fail?
    if "fail" in kwargs.keys():
        if kwargs["fail"]==True:
            fail = True
    else:
        fail = False
        try:
            kwargs["static_time"]
            t = 1
        except:
            t = randint(0,3)   # random waiting time between 0 and 3 sec
    if fail==True:
        e = f"Dummy Error\n\t[args]={args}\n\t[kwargs]={kwargs}"
        raise Exception(e)
    else:
        time.sleep(t)
    ## response
    if debug==True: print("time=",t)
    if debug==True: print("args=",args)
    if debug==True: print("kwargs=",kwargs)
    resp = dict()
    if len(kwargs)>0:
        resp = kwargs.copy()
    if len(args)>0:
        resp.update({"args": args})
    resp.update({"time": t})
    if debug==True: print("*"*50, " End debugging.")
    return resp



## from datatools

import multiprocessing as mp
# import time


def __get_number_of_cores_to_use():
    numbers_of_cores = mp.cpu_count()
    numbers_2_use = numbers_of_cores - int(round(numbers_of_cores*0.2,0))
    if numbers_of_cores==numbers_2_use:
        numbers_2_use = numbers_2_use-1
    print(f"#cores={numbers_of_cores}, #cores to use={numbers_2_use}")
    return numbers_2_use


def function2mp(function, kwargs:list=None, numbers_of_cores:int=None, use_gen:bool=False, debug:bool=False):
    """
        Params:
            function: function to paralalellize
            kwarg: arguments in dict
            number_of_cores:int
            use_gen:bool=False :: (if heavy use of memory should be True)
        Return:
            List of dicts [{"params":params, "response":response, "error":error}]
    """

    def __callback_progress(results):
        # print('|', end='', flush=True)
        # print(f'Callback received: {results}')
        result_lst.append(results)
        print(f"{len(result_lst)}({round(len(result_lst)/len(kwargs)*100,2)}%)  de {len(kwargs)}", end='\r', flush=True)


    if numbers_of_cores==None:
        numbers_of_cores = __get_number_of_cores_to_use()
    else:
        if numbers_of_cores>mp.cpu_count():
            numbers_of_cores = mp.cpu_count()
    if debug==True: print("number of cores for parallelizing", numbers_of_cores)
    results = list()
    result_lst = list()
    # if __name__ ==  '__main__':
    start=time.time()
    with mp.Pool(processes=numbers_of_cores) as p:
        if use_gen==True:
            jobs = ((params, p.apply_async(func=function, kwds=params, callback=__callback_progress)) for params in kwargs)
        else:
            jobs = [(params, p.apply_async(func=function, kwds=params, callback=__callback_progress)) for params in kwargs]
        for params,j in jobs:
            try:
                response = j.get()
                results.append({"params": params, "response": response, "error": None})
                # print(params, response)
            except Exception as e:
                results.append({"params": params, "response": None, "error": str(e)})
                print(params, e)
        # results = [dict((k,v) for k,v in x.items() if v!=None) for x in results]
    # else:
    #     print("__name__ != __main__ --> ",__name__)
    return results

def __test_paralell(a:int,b:int):
    return a+b