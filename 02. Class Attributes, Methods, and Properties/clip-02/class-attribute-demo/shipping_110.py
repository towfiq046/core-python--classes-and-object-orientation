class ShippingContainer:

    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # It's much better and safer to access class attributes
        # as attributes of the class object rather than via the instance.
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
