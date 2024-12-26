class Stock:
    def __init__(self, name, shares, price):
        self.name = name 
        self.shares = shares
        self.price = price 

    
    def cost(self):
        return self.shares * self.price 
    
    def sell(self, n_shares):
        if n_shares > self.shares:
            raise ValueError("Don't have enoough shares to sell")
        
        self.shares -= n_shares 