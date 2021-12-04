from typedproperty import typedproperty


class Stock:
    name = typedproperty("name", str)
    shares = typedproperty("shares", int)
    price = typedproperty("price", float)

    def __init__(self, name, shares, price) -> None:
        self.name = name
        self._shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"Stock({self.name},{self.shares},{self.price})"

    @property
    def cost(self):
        return self.shares * self.price

    # @property
    # def shares(self):
    #     return self._shares

    # @shares.setter
    # def shares(self, shares):
    #     self._shares = shares

    def sell(self, amount):
        if amount <= self.shares:
            self.shares -= amount
        else:
            raise ValueError(f"Tried to sell {amount} of shares out of {self.shares}")
