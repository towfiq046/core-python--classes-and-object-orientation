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

    # Strongly recommended to implement teamly implementing __repr__ especially for object which represent value.
    def __repr__(self):  # Who is __repr__ for, its for developers.
        return f"Position({self.latitude} {self.longitude})"
