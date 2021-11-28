class Stock:
    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"Stock({self.name},{self.shares},{self.price})"

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        if amount <= self.shares:
            self.shares -= amount
        else:
            raise ValueError(f"Tried to sell {amount} of shares out of {self.shares}")
