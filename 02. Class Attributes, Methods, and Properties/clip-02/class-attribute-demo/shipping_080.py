class ShippingContainer:

    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1


c1 = ShippingContainer('ETS', ['tools'])
print(c1.serial)

# We can retrieve the class attribute from outside the class by qualifying it with the class name.
print(ShippingContainer.next_serial)

# We can also retrieve the class attribute through instance of the class.
print(c1.next_serial)
