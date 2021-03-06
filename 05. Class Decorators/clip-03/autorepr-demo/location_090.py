import inspect

from position import EarthPosition
from utility import typename


def auto_repr(cls):
    print(f"Decorating {cls.__name__} with auto_repr")
    members = vars(cls)
    for name, member in members.items():
        print(name, member)
    return cls


@auto_repr # Class decorators are applied when decorated class is first being defined and that happens when module
    # containing the class definition is first imported.
    # Modules in python are singleton, each module only exists once in the memory of a given process.
class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    def __str__(self):
        return self.name


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))
