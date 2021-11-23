class ShippingContainer:

    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # It works but better to avoid it,
        # since it makes less clear to find which is instance attribute and which is class attribute.
        self.serial = self.next_serial
        self.next_serial += 1
