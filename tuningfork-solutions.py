import math

def tuning_frequency(material, youngs_mod, density):
    '''
    Calculate the first vibrational mode of a tuning fork made of a material
    given the Young's Modulus (N/m^2) and density (kg/m^3) of the material.
    
    The tuning fork is 107 mm long and 7.2 mm thick throughout.
    '''

    pre_factor = 0.162
    L = 107e-3 #meters
    a = 7.2e-3 #meters

    constant = pre_factor * (a/(L**2))

    sqrt_term = math.sqrt(youngs_mod/density)

    frequency = constant * sqrt_term

    return frequency


def load_material_properties(filename):
    '''
    Load csv data of material names, young's modulus, and density into a Python
    dictionary.
    
    The keys of the materials dictionary are the names of materials and the
    value of each is a tuple of (Young's Modulus, Density).
    '''
    materials_dictionary = {}
    file = open(filename)
    data = file.readlines()
    file.close()
    
    for line in data:
        key, yModulus, density = line.strip('\n').split(',')
        materials_dictionary[key] = (float(yModulus), float(density))

    return materials_dictionary


materials = load_material_properties('materials- youngs modulus-densities.txt')

max_material = ''
max_frequency = 0

for material, properties in materials.items():
    calculated_frequency = tuning_frequency(material, properties[0],
                                            properties[1])
    if calculated_frequency > max_frequency:
        max_frequency = calculated_frequency
        max_material = material

print('%s produces the highest frequency. f_1 = %f' %(max_material,
                                                      max_frequency))
