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
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    # In other languages constructors at every level in an inheritance hierarchy
    # will be called automatically, same can't be said for initializers in python.
    def __init__(self, owner_code, contents, celsius):
        # If we want the base class initializers to be called when we override
        # the initializer in a derived class we must do so explicitly.
        # Explicit is better than implicit.
        super().__init__(owner_code, contents)  # To get a reference to the base class instance.
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self.celsius = celsius

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )


r1 = RefrigeratedShippingContainer('YDS', ['eggs'], 15)
print(r1)
