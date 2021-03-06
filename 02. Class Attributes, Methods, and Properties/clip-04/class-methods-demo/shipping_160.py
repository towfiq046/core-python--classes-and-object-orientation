class ShippingContainer:

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):  # cls refers to class object.
        result = cls.next_serial
        cls.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()
