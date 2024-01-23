class Pizza:
    def __init__(self, uid=None, toppings=[]) -> None:
        self.uid = uid
        self.toppings = toppings
        self.served = False


pepperonidream = Pizza()


