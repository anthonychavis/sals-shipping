# from typing import Optional, Union
# from typing import TypedDict
def find_lowest_shipping(weight: int | float = 0):
  '''inform customer of the lowest cost method of shipping their package based on its weight'''
  if not isinstance(weight, (int, float)): 
    print(f'🚨 You entered "{weight}"; only positive numerical values (int, float), or 0, are allowed. 🚨\n')
    return
  if weight < 0: 
    print(f'🚨 You entered "{weight}", but the minimum allowed weight is 0 lbs. 🚨\n')
    return
  MultipliersTuple = tuple[float]  # check !!
  ShippingDict = dict[str, float | MultipliersTuple]  # check !!
  # check !! PEP 589
  # class ShippingDict(TypedDict):
  #   flat_fee: float
  #   multipliers: tuple(float)
  ground:ShippingDict = {
    'shipping_type': 'Standard Ground Shipping',
    'flat_fee': 20.,
    'multipliers': (1.5, 3., 4., 4.75),
    'shipping_cost': 0.
  }
  drone: ShippingDict = {
    'shipping_type': 'Drone Shipping',
    'flat_fee': 0.,
    'multipliers': (4.5, 9., 12., 14.25),
    'shipping_cost': 0.
  }
  premium: ShippingDict = {
    'shipping_type': 'Premium Ground Shipping',
    'shipping_cost': 125.
  }
  def shipping_cost_fxn(weight: int | float, shipping_type: str, flat_fee: float, multipliers: MultipliersTuple, shipping_cost: float):
    """calculate shipping cost based on package weight when shipped via drone or standard ground"""
    if weight <=2: flat_fee += weight * multipliers[0]
    elif weight <= 6: flat_fee += weight * multipliers[1]
    elif weight <= 10: flat_fee += weight * multipliers[2]
    else: flat_fee += weight * multipliers[3]
    return flat_fee
  # print(type(MultipliersTuple))
  # print(type(ShippingDict))
  ground["shipping_cost"] = shipping_cost_fxn(weight, **ground)
  drone["shipping_cost"] = shipping_cost_fxn(weight, **drone)
  def myFunc(e):
    return e['shipping_cost']
  lowest = [premium, ground, drone]
  lowest.sort(key=myFunc)
  print(f'For a package weighing {weight} lbs, {lowest[0]["shipping_type"]} saves you the most money. The total cost would be ${"{:.2f}".format(lowest[0]["shipping_cost"])}.\n{lowest[1]["shipping_type"]} would cost ${"{:.2f}".format(lowest[1]["shipping_cost"])}.\n{lowest[2]["shipping_type"]} would be the most expensive option at ${"{:.2f}".format(lowest[2]["shipping_cost"])}.\n')
  # print(locals())

# static code analysis !!