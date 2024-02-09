# from typing import Optional, Union
# from typing import TypedDict
def find_lowest_shipping(weight: int | float = 0):
  '''inform customer of the lowest cost method of shipping their package based on its weight; input must be a positive int or float not exceeding 10 digits'''
  def input_err_mssg(weight: int | float, mssg_piece:str): return f'🚨 You entered "{weight}"{mssg_piece}. 🚨\n'
  if len(str(weight).replace('.', '', 1)) > 10:
    print(input_err_mssg(weight, ' which exceeds the allowed 10 number of digits'))
    return
  if not isinstance(weight, (int, float)): 
    print(input_err_mssg(weight, '; only positive numerical values, or 0, are allowed'))
    return
  if weight < 0: 
    print(input_err_mssg(weight, ', but the minimum allowed weight is 0 lbs'))
    return
  MultipliersTuple = tuple[float]  # check !!
  ShippingDict = dict[str, float | MultipliersTuple]  # fix & check !!
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
  teleportation: ShippingDict = {
    'shipping_type': 'Teleportation Shipping',
    'shipping_cost': 500.
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
  def cost_sort(e: ShippingDict):
    """Used when sorting 'lowest'. Return the value of shipping_cost if it exists; otherwise return -1 so the dict is at the beginning when 'lowest' is sorted in ascending order"""
    if "shipping_cost" in e:
      return e['shipping_cost']
    else:
      print(f'{e["shipping_type"]} shipping_cost undefined')
      return -1
  lowest = [premium, teleportation, ground, drone]
  lowest.sort(key=cost_sort)
  mssg_to_user = f'For a package weighing {weight} lbs:\n'
  count = 0
  error_count = 0
  lowest_len = len(lowest) - 1
  # for i, x in enumerate(lowest):
  for x in lowest:
    # print(count," - ", len(lowest))
    if not "shipping_cost" in x:
      mssg_to_user += f'🚨 shipping_cost undefined for {x["shipping_type"]} 🚨\n'
      error_count += 1
      continue
    elif count == 0:
      mssg_to_user += f'• {x["shipping_type"]} saves you the most money. The total cost would be ${"{:.2f}".format(x["shipping_cost"])}.\n'
    elif count == lowest_len - error_count: 
      mssg_to_user += f'• {x["shipping_type"]} would be the most expensive option at ${"{:.2f}".format(x["shipping_cost"])}.\n'
    else:
      mssg_to_user += f'• {x["shipping_type"]} would cost ${"{:.2f}".format(x["shipping_cost"])}.\n'
    count += 1
  print(mssg_to_user)
  # print(locals())
  return

# static code analysis !!