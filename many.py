import parallel
import logging

def many(backends, files, timeout=None):
    res = []
    for i,f in enumerate(files):
        r = parallel.parallelize(backends, f, timeout=timeout)
        res.append(r)
        if r.done:
            print(f'Done: {i+1}/{len(files)}')
        else:
            print(f'Not Done: {i+1}/{len(files)}, Reason: {r.error}')
    print("Done")
    return res
        