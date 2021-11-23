class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def __repr__(self):
        return f"Position({self.latitude}, {self.longitude})"


p = Position(25.5, 58.3)
r = repr(p)
print(type(r))
print(r)  # Evaluating __repr__ of p, the result of the call to __repr__ is a string.
print(type(p))
print(p)  # Evaluating p alone we get __repr__ of p.


# When the python repl needs to display the result of an expression it requests the __repr__ of the result.

