class ShippingContainer:

    next_serial = 1337

    def __init__(self, owner_code, contents):
        # Assigning to an instance attribute is how we create an instance attribute.
        self.owner_code = owner_code
        self.contents = contents
        # We can read class attribute through self instance reference.
        # But we can not assign to class attribute through self instance reference.

        # If we attempt to assign to an existing class attribute through self reference
        # we would create a new instance attribute. It will hide the class attribute.
        # Class attribute would remain unmodified.

        # Augmented assignment operator is not assignment,
        # it works as a read, modify and write operation which modifies the existing object.
        self.serial = self.next_serial
        self.next_serial = self.next_serial + 1  # This would create instance attribute as well as class attribute.
        # Instance attribute takes precedence over the class attribute when accessed through self.
