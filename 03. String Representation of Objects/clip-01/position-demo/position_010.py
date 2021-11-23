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


p = Position(60, 70)
print(repr(p))
print(str(p))
print(format(p))

# There isn't any string conversion behaviour defined.
# Thy are all inherited from object base class from which Position class implicitly inherits.
