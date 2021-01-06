from typing import Any

foolist: Any
foovar: Any
list_with_none: Any
none: Any

class Base:
    Inner: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, val: str) -> None: ...

class CppException(Exception): ...

class Derived(Base):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def count(self) -> int: ...
    @count.setter
    def count(self, val: int) -> None: ...

class Foo:
    FooChild: Any = ...
    def __init__(self) -> None: ...
    def f(self) -> None: ...

class Outer:
    Inner: Any = ...
    linalg: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def inner(self) -> python_example.Outer.Inner: ...
    @inner.setter
    def inner(self, val: python_example.Outer.Inner) -> None: ...
