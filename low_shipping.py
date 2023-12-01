# weight = 1.5
# weight = 4.8
# weight = 41.5

def find_lowest_shipping(weight):
  # Ground Shipping
  ground_shipping_cost = 20.
  if (weight <= 2):
    ground_shipping_cost += weight * 1.5
  elif (weight <= 6):
    ground_shipping_cost += weight * 3.
  elif (weight <= 10):
    ground_shipping_cost += weight * 4.
  else:
    ground_shipping_cost += weight * 4.75

  premium_ground_shipping = 125.

  # ground_shipping_cost = round(ground_shipping_cost, 2)
  print('Ground: $' + "{:.2f}".format(ground_shipping_cost))

  # print('Ground Shipping Premium $' + '{:.2f}'.format(premium_ground_shipping))
  # print('Ground Shipping Premium $%s' %"{:.2f}".format(premium_ground_shipping))

  # Drone Shipping
  per_lb_drone = 0.
  if (weight <= 2):
    per_lb_drone += weight * 4.5
  elif (weight <= 6):
    per_lb_drone += weight * 9.
  elif (weight <= 10):
    per_lb_drone += weight * 12.
  else:
    per_lb_drone += weight * 14.25

  print('Drone: $' + '{:.2f}'.format(per_lb_drone))

  conditions = (ground_shipping_cost, 'Ground Shipping') if ground_shipping_cost < per_lb_drone else (per_lb_drone, 'Drone Shipping')

  print(f'The lowest cost method of shipping for a package that weighs {weight} lbs is %s at $%s' %(conditions[1] if conditions[0] < premium_ground_shipping else 'Premium Ground Shipping', '{:.2f}'.format(conditions[0]) if conditions[0] < premium_ground_shipping else "{:.2f}".format(premium_ground_shipping)))
