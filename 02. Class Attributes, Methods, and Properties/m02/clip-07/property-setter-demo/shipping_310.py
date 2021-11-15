import iso6346


class ShippingContainer:

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)

    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents, **kwargs)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = celsius

    @property
    def celsius(self):  # Getter.
        return self._celsius

    # Here celsius is the property object.
    @celsius.setter
    # Decorator specific to the property, which is itself an attribute of the
    # property object that was created when we defined the getter.
    # Its called setter and must be called via the property object.
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )

# Decorating function with @p.setter causes the property object to be modified associating with our
# setter method in addition to the getter method.

# When we decorate our celsius getter with property the returned object is also bound to the name celsius, it is this
# returned property object which has the setter attribute attached to it which is another decorator, which is used to
# decorate our setter definition.


r = RefrigeratedShippingContainer.create_with_items('IER', 'eggs', celsius=-22)

print(r.celsius)
print('\n')
r.celsius = 10
