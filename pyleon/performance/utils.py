import copy

class CopyCached(object):
    '''
    from pyleon.performance.utils import CopyCached
    '''
    def __init__(self, obj, cache=10):
        self._no_calls = 0
        self._objs = [copy.copy(obj) for i in range(cache)]

    def __call__(self):
        val =  self._objs[self._no_calls]
        self._no_calls += 1
        return val
