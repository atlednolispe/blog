import cProfile, pstats
import time

from django.utils.six import StringIO


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