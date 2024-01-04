def find_lowest_shipping(weight: int | float = 0):
  if not isinstance(weight, (int, float)) or weight < 0:
    raise TypeError('You entered {}; only positive numerical values (int, float), or 0, are allowed.'.format(weight))
  def shipping_cost(weight: int | float, ship_method='drone'):
    """calculate shipping cost based on package weight when shipped via drone or standard ground"""
    ground_shipping_cost = 20.
    drone_shipping_cost = 0.
    ground_multipliers = (1.5, 3., 4., 4.75)
    drone_multipliers = (4.5, 9., 12., 14.25)
    multipliers = ground_multipliers if ship_method == 'ground' else drone_multipliers
    cost = ground_shipping_cost if ship_method == 'ground' else drone_shipping_cost
    if weight <=2: cost += weight * multipliers[0]
    elif weight <= 6: cost += weight * multipliers[1]
    elif weight <= 10: cost += weight * multipliers[2]
    else: cost += weight * multipliers[3]
    # return '{}: $'.format(ship_method) + "{:.2f}".format(cost)
    return cost
  ground_shipping_cost = shipping_cost(weight, 'ground')
  drone_shipping_cost = shipping_cost(weight)
  premium_ground_shipping = 125.
  conditions = (ground_shipping_cost, 'Ground Shipping') if ground_shipping_cost < drone_shipping_cost else (drone_shipping_cost, 'Drone Shipping')
  print(f'The lowest cost method of shipping for a package that weighs {weight} lbs is %s at $%s' %(conditions[1] if conditions[0] < premium_ground_shipping else 'Premium Ground Shipping', '{:.2f}'.format(conditions[0]) if conditions[0] < premium_ground_shipping else "{:.2f}".format(premium_ground_shipping)))
