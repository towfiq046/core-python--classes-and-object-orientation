class MyClass:

    b = "on class"

    def __init__(self):
        self.a = "on instance"
        print(self.a)  # Via the instance object reference self.

        print(MyClass.b)  # Via the class object reference MyClass.

        print(self.b)   # Class attribute can also be accessed via the instance object reference self.

        self.a = "re-bound"  # Assigning to self.a rebinds the instance attribute to a new value.

        self.b = "new on instance"  # Assigning to self.b does not rebind the class attribute to a new value,
        # instead it creates a new instance attribute which hides the class attribute.
        # Instance attribute takes precedence over class attribute when accessed through self.

        print(self.b)  # Accesses the instance attribute instead class attribute.
        print(MyClass.b)  # To unambiguous refer to class attribute we should refer to class object reference.
