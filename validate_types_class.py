from typing import get_type_hints, Dict
from dataclasses import dataclass

def validate_generic_type(expected_type, value):
    """Validates a generic type. Current implementation only supports Dict type."""
    if not isinstance(value, expected_type.__origin__):
        raise TypeError(f"Invalid argument type. Expected {expected_type.__origin__}. Got {type(value)}.")
    else:
        if hasattr(expected_type, '__args__'):
            if expected_type.__origin__ == dict:
                key_type, value_type = expected_type.__args__
                if hasattr(key_type, '__origin__'):
                    for key in value.keys():
                        validate_generic_type(key_type, key)
                else:
                    for key in value.keys():
                        if not isinstance(key, key_type):
                            raise TypeError(f"Invalid argument type for dict key. Expected {key_type}. Got {type(key)}.")
                if hasattr(value_type, '__origin__'):
                    for val in value.values():
                        validate_generic_type(value_type, val)
                else:
                    for val in value.values():
                        if not isinstance(val, value_type):
                            raise TypeError(f"Invalid argument type for dict value. Expected {value_type}. Got {type(val)}.")
            

def validate_types(func):
    def wrapper(*args, **kwargs):
        annotations = get_type_hints(func)

        for name, expected_type in annotations.items():
            if name in kwargs:
                if hasattr(expected_type, '__origin__'):
                    validate_generic_type(expected_type, kwargs[name])
                else:
                    if not isinstance(kwargs[name], expected_type):
                        raise TypeError(f"Invalid argument type for {name}. Expected {expected_type}.")

        return func(*args, **kwargs)

    return wrapper

def validate_types_class(cls):
    for name, attr in cls.__dict__.items():
        if callable(attr):
            setattr(cls, name, validate_types(attr))
    return cls

@validate_types
def a_func(x: int, y: float, bla: Dict[str,Dict[str,Dict[str,str]]]) -> bool:
    return False

@validate_types_class
@dataclass
class AClass:
    a: int
    b: float
    c: Dict[str,Dict[str,Dict[str,str]]]
    
    def a_method(self, x: int, y: float, z: str) -> bool:
        return False


a_func(x=1, y=2.0, bla={'a':{'b':{'c':'d'}}})
a = AClass(a=1, b=2.0, c={'a':{'b':{'c':'d'}}})
b = AClass(a=10, b=2.7, c={'b':{'b':{'c':'d'}}})
a.a_method(x=1, y=2.0, z='3')
