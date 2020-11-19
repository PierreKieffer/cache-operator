import time
"""
cache_operator
"""
def cache(method): 
    cached_data = {}
    def wrapper(*args, **kwargs): 

        clean = kwargs.get("clean_cache", False)
        if clean : 
            cached_data.clear()

        else: 
            key = str(args) + str(kwargs)
            if key in cached_data:
                return cached_data[key]
            else : 
                r = method(*args, **kwargs)
                cached_data[key] = r
                return r
    return wrapper


