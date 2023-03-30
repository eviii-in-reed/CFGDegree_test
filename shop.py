class NotEnoughMoneyError(Exception):
    pass

class MaxPurchaseAttemptsExceededError(Exception):
    pass

def purchase_item(item, available_money):
    prices = {
        "pen": 50,
        "notebook": 150,
        "backpack": 200
    }

    if item not in prices:
        raise ValueError("Invalid item selected")

    price = prices[item]

    if price > available_money:
        raise NotEnoughMoneyError("You don't have enough money to purchase this item")

    print(f"Here's your {item}!")
    return available_money - price

def shop():
    available_money = 100
    purchase_attempts = 0

    print("Welcome to the shop!")
    print("Items and their prices:")
    print("- Pen: £50")
    print("- Notebook: £150")
    print("- Backpack: £200")
    print("Enter the name of the item you want to purchase, or type 'exit' to leave the shop")

    while True:
        item = input("> ").lower()

        try:
            if item == "exit":
                break
            available_money = purchase_item(item, available_money)
            purchase_attempts += 1
            print(f"You have £{available_money} left")
        except ValueError as e:
            print(str(e))
        except NotEnoughMoneyError as e:
            print(str(e))
            if purchase_attempts < 1:
                try:
                    response = input("Do you have more money? (yes/no) ").lower()
                    if response == "yes":
                        additional_money = int(input("Enter the amount of additional money you have: "))
                        available_money += additional_money
                        print(f"You now have £{available_money}")
                    if response == "no":
                        break
                except:
                    raise ValueError("Please input 'yes' or 'no'")
            else:
                raise MaxPurchaseAttemptsExceededError("You have exceeded the maximum number of purchase attempts (3)") from e

    print("Thank you for visiting the shop!")


if __name__ == "__main__":
    shop()
