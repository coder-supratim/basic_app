

def test_mutable_datatype():
    # Test case for mutable datatype (list)
    my_list = [1, 2, 3]
    print(f"id of my_list before append: {id(my_list)}")
    my_list.append(4)
    assert my_list == [1, 2, 3, 4]
    print(f"id of my_list after append: {id(my_list)}")
    assert id(my_list) == id(my_list)  # ID should remain the same after mutation
    my_list = [5, 6]
    print(f"id of my_list after reassignment: {id(my_list)}")
test_mutable_datatype()


def explain_number_datatypes():
    # Explanation of number datatypes in Python
    int_num = 10          # Integer
    float_num = 10.5     # Floating-point number
    complex_num = 2 + 3j # Complex number

    print(f"Integer: {int_num}, Type: {type(int_num)}")
    print(f"Float: {float_num}, Type: {type(float_num)}")
    print(f"Complex: {complex_num}, Type: {type(complex_num)}")
   #integer division
    a = 7
    b = 3
    int_div = a // b # Integer Division without decimal part
    float_div = a / b # Float Division with decimal part
    remainder = a % b # Remainder of the division
    print(f"Integer Division of {a} // {b} = {int_div}")
    print(f"Float Division of {a} / {b} = {float_div}")
    print(f"Remainder of {a} % {b} = {remainder}")
explain_number_datatypes()