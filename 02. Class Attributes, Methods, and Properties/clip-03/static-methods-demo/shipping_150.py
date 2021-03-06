class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()  # Explicit is better than implicit.


c1 = ShippingContainer('UHO', ['coffee'])
print(f'Serial: {c1.serial}')
print(f'Next serial: {c1.next_serial}')
print(f'Next serial: {ShippingContainer.next_serial}')
