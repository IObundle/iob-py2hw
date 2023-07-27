class iob_datum:
    """Class to represent a data item"""
    def __init__(self, name="", width=1, value=0):
        self.name = name
        self.width = width
        self.value = value

def unit_test():
    """Unit test for iob_datum"""
    
    # Print title
    print("Unit test for iob_datum:")
    
    # Create a data item
    data0 = iob_datum("data0", 8, 6)
    # Check if the data item is correct
    assert data0.name == "data0"
    assert data0.width == 8
    assert data0.value == 6

    # Create a data item with string value type
    data1 = iob_datum("data1", 8, "a")
    # Check if the data item is correct
    assert data1.name == "data1"
    assert data1.width == 8
    assert data1.value == "a"

    # Create a data item with object value type
    data2 = iob_datum("data2", 8, data0)
    # Check if the data item is correct
    assert data2.name == "data2"
    assert data2.width == 8
    assert data2.value == data0
    
    # Print the data item
    print(f"Name: {data0.name}, width: {data0.width}, value: {data0.value}")
    print(f"Name: {data1.name}, width: {data1.width}, value: {data1.value}")
    print(f"Name: {data2.name}, width: {data2.width}, value: {data2.value}")
    # Print end of unit test
    print("End of unit test for iob_datum.\n")

if __name__ == "__main__":
    unit_test()
