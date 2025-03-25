class Category:
    # Assign the initial values in the constructor 
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.deposited = 0
        self.total = 0
    
    # Build and format what the receipt will display, mimicking what a recepit would look like
    def __str__(self):
        receipt = self.category.center(30, "*") + "\n"
        for statement in self.ledger:
            receipt += statement["description"][:23] + f"{statement['amount']:.2f}".rjust(30 - len(statement["description"][:23])) + "\n"

        receipt += f"Total: {self.get_balance()}"
        return receipt
    
    # Add money to deposit
    def deposit(self, amount, description = ""):
        # Add money to account and document onto the ledger
        self.deposited += amount
        self.ledger.append({ "amount": amount, "description": description })

    # Withdraw money from account
    def withdraw(self, amount, description = ""):
        #  If user will go to negative, stop the 'withdrawal' 
        if self.check_funds(amount) == False:
            return False
        else:
            # Document the withdrawal onto the ledger
            self.ledger.append({ "amount": amount*-1, "description": description })
            return True

    # Retrieve the balance for the user
    def get_balance(self, accountSum = 0, i = 0):
        # Runs this recursively to get the balance without a for loop
        if i < len(self.ledger):
            accountSum += self.ledger[i]["amount"]
            accountSum = self.get_balance(accountSum, i+1)
        
        return accountSum

    # Let's user transfer to a different account if they have the fund
    def transfer(self, amount, destinationBudget):
        #  If user will go to negative, stop the 'transfer'
        if self.check_funds(amount) == False:
            return False
        else:
            # Document the transfers on both accounts
            destinationBudget.deposit(amount, f"Transfer from {self.category}")
            self.withdraw(amount, f"Transfer to {destinationBudget.category}")
            return True

    # Checks user's balance compared withdrawal or transfer amount
    def check_funds(self, amount):
       return False if amount > self.get_balance() else True
   
    # Retrieve the withdrawal total the user has done through the life of the account
    def get_withdrawals(self, withdrawals = 0, i = 0):
       # Only sum the withdrawals from this account
        if i < len(self.ledger):
            withdrawals += self.ledger[i]["amount"] if self.ledger[i]["amount"] < 0 else 0
            withdrawals = self.get_withdrawals(withdrawals, i+1)

        return withdrawals

# Builds the vertical titles for the graph
def format_titles(longestTitle, columns, category):
    # Loop that sets the vertical titles
    # TODO: future me wants to improve this
    for i in range(longestTitle):
        if i in columns and i < len(category.category):
            columns[i] += f" {category.category[i]} "
        elif i < len(category.category):
            columns[i] = f"     {category.category[i]} "
        elif i in columns:
            columns[i] += "   "
        else:
            columns[i] = "       "

    return columns

# Build the graph's 'y' and 'x' axis
# TODO: I would want to come back to this later to refactor
def format_graph(barGraph, categories, columns):
    chart = "Percentage spent by category\n"
    
    # Layering each line with the y axis and bar value
    for key in barGraph:
        chart += (f"{(key + '|').rjust(4)}{barGraph[key]}\n")

    # Builds the x axis of the divider
    divider = "    -"
    for i in range(len(categories)):
        divider += "---"
    
    # Adding the verticle titles that are respective to their location
    setTitles = "\n"
    for i, column in enumerate(columns):
        setTitles += columns[column] + " \n" if i < len(columns)-1 else columns[column] + " "

    chart += f"{divider}{setTitles}"
    return chart
    
# Main function to build the graph
def create_spend_chart(categories):
    # Start building the scaffolding of the graph to eventually put it all together 
    columns = {}
    barGraph = {f"{num*10}": "" for num in range (10, -1, -1)}
    longestTitle = len(max([category.category for category in categories], key=len))
    totalSpent = sum(category.get_withdrawals() for category in categories)
    
    # Build and stich pars of the graph together
    for i, category in enumerate(categories):
        withdrawals = category.get_withdrawals()
        bars = round(((withdrawals / totalSpent) * 100))

        for key in barGraph:
            barGraph[key] += "o".center(3) if int(key) <= bars else "".center(3)
            barGraph[key] += " " if i == len(categories)-1 else ""
            
        columns = format_titles(longestTitle, columns, category)

    # Build and put finishing parts of the graph together and return it back to the user
    return format_graph(barGraph, categories, columns)
