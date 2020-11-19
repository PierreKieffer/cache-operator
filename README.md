# cache-operator
cache-operator allows to cache the return values of a function depending on the arguments.
It can save time when an I/O bound function is periodically called with the same arguments.


## Install 
```bash
pip install .
```

## Usage
```python
# import
from cache_operator import cache

# call cache decorator
@cache
def worker(*args, **kwargs): 
    pass

# To clean cache for associated method, call the method with clean_cache=True
```

Example:
```python
from cache_operator import cache
import time

@cache
def worker(i, k=2): 
    print("computing ...")
    time.sleep(2)
    return i*k 

if __name__=="__main__":

    print("First run")
    res = worker(1,2)
    print(res)
    print("------------")

    print("Second run")
    res = worker(1,2)
    print(res)

    print("Clean cache")                                                                                              
    worker(clean_cache=True)
```

Output : 
```
First run
computing ...
2
------------
Second run
2

```


