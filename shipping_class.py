class Find_Lowest_Shipping:
    def __init__(self, weight: int | float = 0) -> None:
        self.__weight = weight
        self.__drone_shipping_cost: float
        self.__ground_shipping_cost: float
        self.__premium_ground_shipping = 125.
    @property
    def weight(self):
        """the 'weight' property"""
        return self.__weight
    @weight.setter
    def weight(self, weight):
        if not isinstance(weight, (int, float)) or weight < 0:
            raise TypeError(f'You entered {weight}; only a single, positive numerical value, or 0, is allowed.')  # needs improvement (see tuple w/ multi-items) !!
        else:
            self.__weight = weight
    @property
    def ground_shipping_cost(self):
        """the 'ground_shipping_cost' property"""
        return self.__ground_shipping_cost
    @ground_shipping_cost.setter
    def ground_shipping_cost(self, cost: float):
        self.__ground_shipping_cost = cost
    @property
    def drone_shipping_cost(self):
        """the 'drone_shipping_cost' property"""
        return self.__drone_shipping_cost
    @drone_shipping_cost.setter
    def drone_shipping_cost(self, cost: float):
        self.__drone_shipping_cost = cost
    @property
    def premium_ground_shipping(self):
        """the 'premium_ground_shipping' property"""
        return self.__premium_ground_shipping
    def ground_shipping_total(self):
        """determine ground shipping cost based on package weight"""
        self.ground_shipping_cost = 20.
        if self.weight <= 2: self.ground_shipping_cost += self.weight * 1.5
        elif self.weight <= 6: self.ground_shipping_cost += self.weight * 3.
        elif self.weight <= 10: self.ground_shipping_cost += self.weight * 4.
        else: self.ground_shipping_cost += self.weight * 4.75
    def drone_shipping_total(self):
        """determine drone shipping cost based on package weight"""
        self.drone_shipping_cost = 0.
        if self.weight <= 2: self.drone_shipping_cost +=  self.weight * 4.5
        elif self.weight <= 6: self.drone_shipping_cost +=  self.weight * 9.
        elif self.weight <= 10: self.drone_shipping_cost +=  self.weight * 12.
        else: self.drone_shipping_cost +=  self.weight * 14.25
    def compare_mssg(self, shippin_type: str, cost: float):
        """lowest cost shipping message"""
        return f'The lowest cost method of shipping for a package weighing {self.weight} lbs is {shippin_type} at ${"{:.2f}".format(cost)}.'
    def compare_costs(self):
        """compare shipping cost of the 3 means of shipping based on package weight"""
        self.ground_shipping_total()
        self.drone_shipping_total()
        if self.premium_ground_shipping <= self.ground_shipping_cost and self.premium_ground_shipping <= self.__drone_shipping_cost: return self.compare_mssg('Premium Ground Shipping', self.premium_ground_shipping)
        elif self.__drone_shipping_cost <= self.premium_ground_shipping and self.__drone_shipping_cost <= self.ground_shipping_cost: return self.compare_mssg('Drone Shipping', self.drone_shipping_cost)
        else: return self.compare_mssg('Normal Ground Shipping', self.ground_shipping_cost)
    def __repr__(self) -> str:
        lowest_shipping_mssg = self.compare_costs()
        return f'{lowest_shipping_mssg}'
        
pkg = Find_Lowest_Shipping()