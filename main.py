# ### Rules

# Sort the packages using the following criteria:

# - A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
# - A package is **heavy** when its mass is greater or equal to 20 kg.

# You must dispatch the packages in the following stacks:

# - **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
# - **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
# - **REJECTED**: packages that are **both** heavy and bulky are rejected.

# ### Implementation

#  **`sort(width, height, length, mass)`** (units are centimeters for the dimensions and kilogram for the mass). 
#  This function must return a string: the name of the stack where the package should go. 
# DO NOT USE TERNARY

HIGH_DIMENSION = 150
HIGH_VOLUME = 1000000
HIGH_MASS = 20

def volume(width: float, height: float, length: float):
    #Assuming that all the dimensions are positive
    return width * height * length

def has_high_volume(width: float, height: float, length: float):
    return volume(width, height, length) >= HIGH_VOLUME

def is_high_dimension(dimension: float):
    return dimension >= HIGH_DIMENSION

def is_bulky(width: float, height: float, length: float):
    return (
        has_high_volume(width, height, length) or
        is_high_dimension(width) or
        is_high_dimension(height) or
        is_high_dimension(length)
    )

def is_heavy(mass: float):
    return mass >= HIGH_MASS

def sort(width: float, height: float, length: float, mass: float):
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)
    
    if bulky and heavy:
        return "REJECTED"
    
    if bulky:
        return "SPECIAL"
    
    if heavy:
        return "SPECIAL"
    
    return "STANDARD"