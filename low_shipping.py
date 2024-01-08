from custom_exceptions import NegativeWeightError 
def find_lowest_shipping(weight: int | float = 0):
  '''inform customer of the lowest cost method of shipping their package based on its weight'''
  # if not isinstance(weight, (int, float)) or weight < 0:
    # raise TypeError('You entered {}; only positive numerical values (int, float), or 0, are allowed.'.format(weight))
  ground = {
    'shipping_cost': 20.,
    'multipliers': (1.5, 3., 4., 4.75)
  }
  drone = {
    'shipping_cost': 0.,
    'multipliers': (4.5, 9., 12., 14.25)
  }
  def shipping_cost_fxn(weight: int | float, shipping_cost: float, multipliers: float):
    """calculate shipping cost based on package weight when shipped via drone or standard ground"""
    if weight <=2: shipping_cost += weight * multipliers[0]
    elif weight <= 6: shipping_cost += weight * multipliers[1]
    elif weight <= 10: shipping_cost += weight * multipliers[2]
    else: shipping_cost += weight * multipliers[3]
    # return '{}: $'.format(ship_method) + "{:.2f}".format(shipping_cost)
    return shipping_cost
  try:
    if weight < 0: raise NegativeWeightError(weight)
    ground_shipping_cost = shipping_cost_fxn(weight, **ground)
    drone_shipping_cost = shipping_cost_fxn(weight, **drone)
  except TypeError as e: print(f'💀 this is why on that day, Types were made 🐞\n{e.__class__.__name__}: {e}')
  except Exception as e: print(f'💀 there\'s a {e.__class__.__name__} 🐞\n{e}')
  else:
    premium_ground_shipping = 125.
    conditions = (ground_shipping_cost, 'Ground Shipping') if ground_shipping_cost < drone_shipping_cost else (drone_shipping_cost, 'Drone Shipping')
    print(f'The lowest cost method of shipping for a package that weighs {weight} lbs is %s at $%s' %(conditions[1] if conditions[0] < premium_ground_shipping else 'Premium Ground Shipping', '{:.2f}'.format(conditions[0]) if conditions[0] < premium_ground_shipping else "{:.2f}".format(premium_ground_shipping)))
    print(locals())
  finally: print('🧁')