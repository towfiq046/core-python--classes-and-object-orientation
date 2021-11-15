class MyClass:

    attribute = "class attribute"

    # cls argument for class method similar to self argument for instance method.
    @classmethod
    def my_class_method(cls, message):
        cls.attribute = message  # Access class attributes via cls.
