# from typing import Optional, Union
# from typing import Generic, NotRequired, TypeVar, TypedDict
def find_lowest_shipping(weight: int | float = 0):
  '''inform customer of the lowest cost method of shipping their package based on its weight; input must be a positive int or float not exceeding 10 digits'''
  def input_err_mssg(weight: int | float, mssg_piece: str): return f'🚨 You entered "{weight}"{mssg_piece}. 🚨\n'
  if len(str(weight).replace('.', '', 1)) > 10:
    print(input_err_mssg(weight, ' which exceeds the allowed 10 number of digits'))
    return
  if not isinstance(weight, (int, float)): 
    print(input_err_mssg(weight, '; only positive numerical values, or 0, are allowed'))
    return
  if weight < 0: 
    print(input_err_mssg(weight, ', but the minimum allowed weight is 0 lbs'))
    return
  
  # syntax for Python < 3.12
  # S = TypeVar('S')
  # F = TypeVar('F')
  # class Multipliers(TypedDict, Generic[F]):
  #   multipliers: tuple[F, F, F, F] | None
  # class SingleVals(TypedDict, Generic[S, F]):
  #   shipping_cost: F
  #   shipping_type: S
  #   flat_fee: F
  # class ShippingDict(SingleVals, Multipliers): pass
  # class ShippingDict(TypedDict, Generic[S, F]):
  #   shipping_cost: F
  #   shipping_type: S
  #   flat_fee: F
  #   multipliers: NotRequired[tuple[F, F, F, F]]

  # fine to use classes especially if used to oop
  # ground: ShippingDict = {
  ground = {
    'shipping_type': 'Standard Ground Shipping',
    'flat_fee': 20.,
    'multipliers': (1.5, 3., 4., 4.75),
    'shipping_cost': 0.  # filled w/shipping_cost_fxn
  }
  # drone: ShippingDict = {
  drone = {
    'shipping_type': 'Drone Shipping',
    'flat_fee': 0.,
    'multipliers': (4.5, 9., 12., 14.25),
    'shipping_cost': 0.  # filled w/shipping_cost_fxn
  }
  # premium: ShippingDict = {
  premium = {
    'shipping_type': 'Premium Ground Shipping',
    'flat_fee': 125.,
    'multipliers': None,
    'shipping_cost': 125.,
  }
  # teleportation: ShippingDict = {
  teleportation = {
    'shipping_type': 'Teleportation Shipping',
    'flat_fee': None,
    'multipliers': None, # type: ignore
    'shipping_cost': 500.
  }
  # fix params:
  # def shipping_cost_fxn(weight: int | float, shipping_type: str, flat_fee: float, multipliers: tuple[float, float, float, float], shipping_cost: float):
  def shipping_cost_fxn(weight: int | float, multipliers, flat_fee):
    """calculate shipping cost based on package weight when shipped via drone or standard ground"""
    if weight <=2: return flat_fee + (weight * multipliers[0])  # parentheses to emphasize intention to reader
    if weight <= 6: return flat_fee + (weight * multipliers[1])
    if weight <= 10: return flat_fee + (weight * multipliers[2])
    
    return flat_fee + (weight * multipliers[3])
    
  # print(type(MultipliersTuple))
  # print(type(ShippingDict))
  # ground["shipping_cost"] = shipping_cost_fxn(weight, **ground)
  ground["shipping_cost"] = shipping_cost_fxn(weight, ground['multipliers'], ground['flat_fee'])
  # drone["shipping_cost"] = shipping_cost_fxn(weight, **drone)
  drone["shipping_cost"] = shipping_cost_fxn(weight, drone['multipliers'], drone['flat_fee'])
  # def cost_sort(e: ShippingDict):
  def cost_sort(e):
    """Used when sorting 'shipping_dicts'. Return the value of shipping_cost if it exists; otherwise return -1 so the dict is at the beginning when 'shipping_dicts' is sorted in ascending order"""
    if "shipping_cost" in e:
      return e['shipping_cost']
    else:
      print(f'{e["shipping_type"]} shipping_cost undefined')
      return -1
  shipping_dicts = [premium, teleportation, ground, drone]
  shipping_dicts.sort(key=cost_sort)
  mssg_to_user = f'For a package weighing {weight} lbs:\n'
  count = 0
  error_count = 0
  shipping_dicts_len = len(shipping_dicts) - 1
  # for i, x in enumerate(shipping_dicts):
  for x in shipping_dicts:
    # print(count," - ", len(shipping_dicts))
    if not "shipping_cost" in x:
      mssg_to_user += f'🚨 shipping_cost undefined for {x["shipping_type"]} 🚨\n'
      error_count += 1
      continue
    elif count == 0:
      mssg_to_user += f'• {x["shipping_type"]} saves you the most money. The total cost would be ${"{:.2f}".format(x["shipping_cost"])}.\n'
    elif count == shipping_dicts_len - error_count: 
      mssg_to_user += f'• {x["shipping_type"]} would be the most expensive option at ${"{:.2f}".format(x["shipping_cost"])}.\n'
    else:
      mssg_to_user += f'• {x["shipping_type"]} would cost ${"{:.2f}".format(x["shipping_cost"])}.\n'
    count += 1
  print(mssg_to_user)
  # print(locals())
  return

# static code analysis !!

# find_lowest_shipping('hi')