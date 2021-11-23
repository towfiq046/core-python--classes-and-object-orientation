class MyClass:

    # Define class attributes in the class block.
    # Class attributes are shared with all instance of the class.
    my_class_attribute = "class attributes go here"
    MY_CONSTANT = "they are often class-specific contants"

    def __init__(self):
        self.my_instance_attribute = "instance attributes here"
