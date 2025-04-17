from main import volume, has_high_volume, is_high_dimension, is_bulky, is_heavy, sort

def test_volume():
    # Any dimension with size = 0 should return 0
    assert volume(0, 123, 234) == 0
    assert volume(123, 0, 234) == 0
    assert volume(234, 123, 0) == 0
    
    # Valid volumes
    assert volume(2, 2, 2) == 8
    assert volume(3, 3, 3) == 27
    assert volume(2, 3, 4) == 24
    assert volume(2000, 5000, 1000) == 10000000000
    assert volume(2.1, 2.3, 2.5) == 12.075
    
def test_has_high_volume():
    assert has_high_volume(100, 100, 100) is True
    assert has_high_volume(100, 101, 100) is True
    assert has_high_volume(100, 99, 100) is False
    
    assert has_high_volume(0, 1000000, 1000000) is False
    assert has_high_volume(1000000, 0, 1000000) is False
    assert has_high_volume(1000000, 1000000, 0) is False
    
def test_is_high_dimension():
    assert is_high_dimension(150) is True
    assert is_high_dimension(150.000000001) is True
    assert is_high_dimension(151) is True
    assert is_high_dimension(149.99999999999) is False
    
    assert is_high_dimension(0) is False
    assert is_high_dimension(10000000000) is True
    
def test_is_bulky():
    assert is_bulky(100, 100, 100) is True
    assert is_bulky(100, 101, 100) is True
    assert is_bulky(10, 10, 150) is True
    assert is_bulky(10, 150, 10) is True
    assert is_bulky(150, 10, 10) is True    

def test_is_heavy():
    assert is_heavy(20) is True
    assert is_heavy(20.000000001) is True
    assert is_heavy(21) is True
    assert is_heavy(19.99999999999) is False
    
    assert is_heavy(0) is False
    assert is_heavy(10000000000) is True
    
def test_sort():
    # Rejected situations
    heavy_and_bulky_packages = [
        [100, 100, 100, 20],
        [100, 101, 100, 20.0000000001],
        [10, 10, 150, 21],
        [10, 150, 10, 21],
        [150, 10, 10, 100]
    ]
    
    for package in heavy_and_bulky_packages:
        assert sort(*package) == "REJECTED"
    
    # Special situations
    only_bulky_packages = [
        [100, 100, 100, 10],
        [100, 101, 100, 10],
        [10, 10, 150, 10],
        [10, 150, 10, 10],
        [150, 10, 10, 10]
    ]
    
    for package in only_bulky_packages:
        assert sort(*package) == "SPECIAL"
    
    only_heavy_packages = [
        [10, 10, 10, 20],
        [10, 10, 10, 21],
        [10, 10, 10, 20.0000001]
    ]
    
    for package in only_heavy_packages:
        assert sort(*package) == "SPECIAL"
    
    # Standard situations
    standard_packages = [
        [10, 10, 10, 10],
        [0.00001, 10, 11, 10],
        [1, 10, 10, 19.99999999999]
    ]
    
    for package in standard_packages:
        assert sort(*package) == "STANDARD"
    
    
    
    
    
    