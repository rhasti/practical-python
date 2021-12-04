from .typedproperty import String, Integer, Float


class Stock:
    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"Stock({self.name},{self.shares},{self.price})"

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        if amount <= self.shares:
            self.shares -= amount
        else:
            raise ValueError(f"Tried to sell {amount} of shares out of {self.shares}")
