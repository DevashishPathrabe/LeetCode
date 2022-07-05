class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.current = 0
        self.n = n
        self.discount = discount
        self.dct = {product:price for product, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.current += 1
        discount = self.discount if self.current % self.n == 0 else 0
        total = 0
        for p, a in zip(product, amount):
            total += self.dct[p] * a
        return total * ((100 - discount) / 100)


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)