import cProfile
import pstats
import time

from django.core.cache import cache
from django.utils.six import StringIO


def cache_it(seconds):
    def decorator(func):
        def wrapper(self, *args, **kwargs):  # wrapper's first argument is a concrete instace, always different.
            key = repr((func.__name__, args, kwargs))
            result = cache.get(key)
            if not result:
                print("%s haven't cached!" % func.__name__)
                result = func(self, *args, **kwargs)
                cache.set(key, result, seconds)

            return result
        return wrapper
    return decorator


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, 'cost', time.time() - start)
        return result
    return wrapper


# profile 1
def loop(count):
    result = []
    for i in range(count):
        result.append(i)


if __name__ == '__main__':
    cProfile.run('loop(1000)')

    # profile 2
    pr = cProfile.Profile()

    pr.enable()
    loop(100000)  # test code
    pr.disable()

    s = StringIO.StringIO()
    # sortby = 'cumulative'
    sortby = 'tottime'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
