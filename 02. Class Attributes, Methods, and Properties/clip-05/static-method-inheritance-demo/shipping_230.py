import iso6346

class ShippingContainer:

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


class RefrigeratedShippingContainer(ShippingContainer):

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )


c1 = RefrigeratedShippingContainer('MAE', ['fish'])
print(c1.bic)
# We don't get or override category R in bic code because in constructor
# base class calls _make_bic_code through a specific class (line 33).

# To get polymorphic override behaviour we need to call the static method on an instance.

# Polymorphism with inheritance means that the version of a method call will depend
# on the type of the object on which it is invoked.

c2 = ShippingContainer('EGS', ['food'])
print(c2._make_bic_code('ESD', 2354))

c2 = RefrigeratedShippingContainer('UEW', ['eggs'])
print(c2._make_bic_code('IGF', 1234))
# We get polymorphic behaviour when we call method through an instance not when we call the method through the class
