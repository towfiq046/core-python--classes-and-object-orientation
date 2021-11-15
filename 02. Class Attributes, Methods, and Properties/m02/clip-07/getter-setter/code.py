class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents, **kwargs)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = celsius

    # This is one way to fix the class invariant violation, but this approach is deeply unpythonic.
    # Furthermore, it would require all uses of the celsius attribute to be adjusted to use the method call syntax.
    def get_celsius(self):
        return self._celsius

    def set_celsius(self, value):
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value
