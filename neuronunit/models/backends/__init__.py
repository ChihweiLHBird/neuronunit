import inspect

from .base import Backend

try:
    from .jNeuroML import jNeuroMLBackend
except:
    print('sytactic error in jNeuroMLBackend')

try:
    from .neuron import NEURONBackend
except:
    print('sytactic error in NEURON')


try:
    from .pyNN import pyNNBackend

except:
    print('sytactic error in pyNN')



available_backends = {x.replace('Backend',''):cls for x, cls \
                   in locals().items() \
                   if inspect.isclass(cls) and \
                   issubclass(cls, Backend)}
print(available_backends)
print(pyNNBackend)
