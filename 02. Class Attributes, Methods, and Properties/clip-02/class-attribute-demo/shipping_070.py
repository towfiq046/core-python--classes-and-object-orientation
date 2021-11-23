class ShippingContainer:
    # Classes don't introduce new scope.
    # ShippingContainer is at global or module scope.
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = next_serial
        next_serial += 1


c1 = ShippingContainer('ETS', ['tools'])
print(c1.serial)
