# from shipping_class import pkg
from low_shipping import find_lowest_shipping

weight_inputs = (22.10526315789, 3.33333333333333, 2, 1.5, 4.8, 41.5, 8.07, -0, -8.07, (0), (0, 2), ('zero'), 'zero', 98765432100, 9876543210, '987654321..0')
for weight in weight_inputs:
    find_lowest_shipping(weight)

find_lowest_shipping()


# find_lowest_shipping(22.10526315789)
# print()
# find_lowest_shipping(3.33333333333333)
# print()

# # print(pkg)
# # print(pkg.drone_shipping_cost)
# find_lowest_shipping()
# print()
# # pkg.weight = 2
# # print('hmm')
# # print('hey', pkg)
# # print(pkg.drone_shipping_cost)
# find_lowest_shipping(2)

# # 
# # print(pkg.weight)
# # print(pkg.compare_costs())
# # print(pkg.drone_shipping_cost)
# # 

# print()
# # pkg.weight = 1.5
# # print(pkg)
# find_lowest_shipping(1.5)

# print()
# # pkg.weight = 4.8
# # print(pkg)
# find_lowest_shipping(4.8)

# print()
# # pkg.weight = 41.5
# # print(pkg)
# find_lowest_shipping(41.5)

# print()
# # pkg.weight = 8.07
# # print(pkg)
# find_lowest_shipping(8.07)

# print()
# # pkg.weight = -0
# # print(pkg)
# find_lowest_shipping(-0)

# print()
# # pkg.weight(-8.07)
# # print(pkg)
# find_lowest_shipping(-8.07)

# print()
# # find_lowest_shipping(0)
# # pkg.weight = [0]
# # print(pkg)
# # find_lowest_shipping([0])
# # pkg.weight = (0)
# # print(pkg)
# find_lowest_shipping((0))
# # find_lowest_shipping((2))
# # find_lowest_shipping((1.5))

# print()
# # pkg.weight = (0, 2)
# # print(pkg)
# find_lowest_shipping((0, 2))

# print()
# # pkg.weight = ('zero')
# find_lowest_shipping(('zero'))

# print()
# # pkg.weight = 'zero'
# # print(pkg)
# find_lowest_shipping('zero')
# # find_lowest_shipping(2)

