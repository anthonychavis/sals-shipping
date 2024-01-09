from custom_exceptions import NegativeWeightError 
def find_lowest_shipping(weight: int | float = 0):
  '''inform customer of the lowest cost method of shipping their package based on its weight'''
  try:
    if not isinstance(weight, (int, float)): raise TypeError(f'You entered {weight}; only positive numerical values (int, float), or 0, are allowed.')
    if weight < 0: raise NegativeWeightError(weight)
    ground = {
      # 'shipping_type': 'Standard Ground Shipping',
      'shipping_cost': 20.,
      'multipliers': (1.5, 3., 4., 4.75)
    }
    drone = {
      # 'shipping_type': 'Drone Shipping',
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
    ground_shipping_cost = shipping_cost_fxn(weight, **ground)
    drone_shipping_cost = shipping_cost_fxn(weight, **drone)
  except TypeError as e: print(f'💀 this is why on that day, Types were made 🐞\n{e.__class__.__name__}: {e}')
  except Exception as e: print(f'💀 there\'s a {e.__class__.__name__} 🐞\n{e}')
  else:
    premium = {
      'shipping_type': 'Premium Ground Shipping',
      'shipping_cost': 125.
      }
    
    conditions = (ground_shipping_cost, 'Ground Shipping') if ground_shipping_cost < drone_shipping_cost else (drone_shipping_cost, 'Drone Shipping')
    
    print(f'The lowest cost method of shipping for a package that weighs {weight} lbs is %s at $%s' %(conditions[1] if conditions[0] < premium['shipping_cost'] else premium['shipping_type'], '{:.2f}'.format(conditions[0]) if conditions[0] < premium['shipping_cost'] else "{:.2f}".format(premium['shipping_cost'])))
    # print(locals())
  finally: print('🧁')