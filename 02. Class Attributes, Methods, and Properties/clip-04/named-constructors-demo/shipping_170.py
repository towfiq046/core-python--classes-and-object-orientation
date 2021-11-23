class ShippingContainer:

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    # Technique to support multiple constructors with different behaviours.
    # No need to twist the __init__ method to interpret different forms of argument list.
    # Class object ShippingContainer will be passed as cls argument of named constructor/factory function.
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])  # Named constructor calls the cls object invoking constructor of the
        # class to create a new instance which is returned by the constructor (create_empty).

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()


c1 = ShippingContainer.create_empty('YML')
print(c1)
print(c1.contents)
