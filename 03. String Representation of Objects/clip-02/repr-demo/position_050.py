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
        # Try to format the result to look like the constructor call, which would produce
        # an object with the same value.
        return f"Position(latitude={self.latitude}, longitude={self.longitude})"
        # Here class name is hard coded. In case of inheritance self would be something else.


sydney = Position(-33.9, 151.2)
r = repr(sydney)
print(r)
e = eval(r)
print(e)

print(e is sydney)
