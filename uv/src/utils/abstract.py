from abc import ABC
from dataclasses import dataclass

def _new_abstract(cls, *args, **kwargs):
    if cls == AbstractDataclass or cls.__bases__[0] == AbstractDataclass:
        raise TypeError("Cannot instantiate abstract class.")
    return super(AbstractDataclass, cls).__new__(cls)

@dataclass
class AbstractDataclass(ABC): 
    def __new__(cls, *args, **kwargs): 
        return _new_abstract(cls, *args, **kwargs)

@dataclass(frozen=True)    
class FrozenAbstractDataclass():
    def __new__(cls, *args, **kwargs): 
        return _new_abstract(cls, *args, **kwargs)