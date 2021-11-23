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

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >= 0 else "W"

    def __repr__(self):
        return f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self):
        return (
            f"{abs(self.latitude)}° {self.latitude_hemisphere}, "
            f"{abs(self.longitude)}° {self.longitude_hemisphere}"
        )

    def __format__(self, format_spec):
        # __format__ excepts second argument, we must accept this to match the signature of method we are overriding.
        return "FORMATTED POSITION"

class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


def typename(obj):
    return type(obj).__name__


aconcagua = EarthPosition(-32.7, -70.1)
print(repr(aconcagua))
print(str(aconcagua))

print(format(aconcagua))
# Both f strings and the format() method delegate to the built in format function which in turn delegates to __format__.
print(f'The highest mountain in South America is located at {aconcagua}')
print('The highest mountain in South America is located at {}'.format(aconcagua))

# If we understand the built in format function we can apply the knowledge to f strings and the format method.
