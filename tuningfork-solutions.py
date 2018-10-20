'''
Assume the tuning fork you will make will be 107 mm long and 7.2 mm thick throughout
'''
def frequency(material, youngs_mod, density, verbose = False):
    import math

    '''
    calculate the first vibrational mode of a material
    given the Young's Modulus (N/m^2) and density (kg/m^3) of the
    material
    '''

    pre_factor = 0.162
    L = 107e-3 #meters
    a = 7.2e-3 #meters

    constant = pre_factor * (a/(L**2))

    sqrt_term = math.sqrt(youngs_mod/density)

    frequency = constant * sqrt_term

    if verbose:
        print('The first vibrational mode of %s is f_1 = %f Hz' %(material,frequency))

    return frequency


'''
the keys of materials_dictionary are the names of the materials
the values of each key is a list of [Young's Mod, density (kg/m^3)]
'''

materials_dictionary = {}

file = open('materials- youngs modulus-densities.txt')
data = file.readlines()
file.close()


for line in data:
    key, yModulus, density = line.strip('\n').split(',')

    materials_dictionary[key] = [float(yModulus), float(density)]

print(materials_dictionary)

max_material = ''
max_frequency = 0

for key, value in materials_dictionary.items():
    calculated_frequency = frequency(key, materials_dictionary[key][0], materials_dictionary[key][1])
    if calculated_frequency > max_frequency:
        max_frequency = calculated_frequency
        max_material = key
print('%s produces the highest frequency. f_1 = %f' %(max_material, max_frequency))
