#!/usr/bin/env python3

import asyncio
import multiprocessing.queues
from solvers.result import Result
import multiprocessing
import library
import time
import signal
import sys
import queue
import os
import psutil

def run(backend, input, q, id):
    os.setsid()
    try:
        res = backend(input)
        # print("reached")
        q.put((id, res))
    except Exception as e:
        q.put((id, Result(done=False, error=str(e))))


def parallelize(backends, filecontents, timeout=None) -> Result:
    if len(backends) == 0:
        return Result(done=False,error="No solvers")
    ctx = multiprocessing.get_context("spawn")
    q = ctx.Queue()
    ps = []



    start = time.perf_counter()
    for i,b in enumerate(backends):
        p = ctx.Process(target=run, args=(b, filecontents, q, i))
        p.start()
        ps.append((i,p))
    try:
        (id, res) = q.get(timeout=timeout)
        # print(any( id == i for (i,_) in ps))
        while res.done != True and not (any( id == i for (i,_) in ps) and (len(ps) == 1)):
            (id, res) = q.get(timeout=(timeout - (time.perf_counter()-start)))
        if res.done:
            # print(f'Solved by {res.model}')
            end = time.perf_counter()
            res.time = (end - start)
        else:
            print("Not solved by any")
    except KeyboardInterrupt:
        for (_,p) in ps:
            if p.is_alive():
                try:
                    [x.kill() for x in psutil.Process(p.pid).children()]
                except:
                    pass
                p.terminate()
                p.join()
        res = Result(done=False, error="Interrupted")
    except queue.Empty:
        print("Timeout!")
        for (_,p) in ps:
            if p.is_alive():
                try:
                    [x.kill() for x in psutil.Process(p.pid).children()]
                except:
                    pass
                p.terminate()
                p.join()
        res = Result(done=False, error="Timeout")
    except Exception as e:
        print(e)
        for (_,p) in ps:
            if p.is_alive():
                try:
                    [x.kill() for x in psutil.Process(p.pid).children()]
                except:
                    pass
                p.terminate()
                p.join()
        res = Result(done=False, error=str(e))

    for (pr,p) in ps:
        if p.is_alive():
            try:
                [x.kill() for x in psutil.Process(p.pid).children()]
            except:
                pass
            p.terminate()
            p.join()
    
    # print(res)
    return res
         


if __name__ == "__main__":
    with open("benchmarks/qurt.c.25.smt2", "r") as f:
            smtfile = f.read()

    res = parallelize([library.solvers["z3"], library.solvers["cvc5"]], smtfile)
    print(res)


