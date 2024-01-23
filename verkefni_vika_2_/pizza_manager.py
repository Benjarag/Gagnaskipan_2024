from pizza import Pizza


class PizzaManager:
    def __init__(self):
        self.pizzas = []
        self.counter = []

    def add_pizzas(self, toppings):
        # will add toppings to pizza and store it for the pizza
        count = 1

        toppings = (
            input("Input toppings (1-3), write each topping with a space inbetween: ")
            .replace(" ", ",")
            .split(",")
        )

        pizza = Pizza()

        if len(toppings) >= 1 or len(toppings) <= 3:
            pizza.toppings = toppings

            if count == 1000:
                pizza.uid = count
                count = 1
            count += 1

        else:
            return None

    def get_all_pizzas(self):
        # returns all the pizzas
        return self.pizzas

    def mark_served_pizza(self, id):
        # marks a pizza served using the id
        for pizza in self.pizzas:
            if pizza.uid == id:
                pizza.served = True

    def remove_all_served_pizzas(self):
        # removes all served pizza
        for pizza, index in enumerate(self.pizzas):
            if pizza.served is True:
                pizza.pop(index)



# unit tests
    # import class into unit tests
# have a sequens diagram to work by
# 