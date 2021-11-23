class ShippingContainer:

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty_container(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_container_with_items(cls, owner_code, contents):
        return cls(owner_code, list(contents))

    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self._contents = contents
        self._serial = ShippingContainer._generate_serial()


c1 = ShippingContainer.create_empty_container('EFS')
print(c1)
print(c1._contents)

c2 = ShippingContainer.create_container_with_items('TAG', ('a', 'b', 'c'))
print(c2)
print(c2._contents)
