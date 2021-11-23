class ShippingContainer:

    next_serial = 1337

    # The idea is to associate _generate_serial with the class not to instance of the class.
    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self._generate_serial()
