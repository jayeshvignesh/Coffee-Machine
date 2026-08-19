from resources import MENU
from resources import resources
from sys import exit
import functions
on = True
def main():
    while on:
        coffee = input("What would you like? (espresso / latte / cappuccino): ").lower().strip()
        if coffee == "off":
            exit()
        if coffee == "report":
            print(resources)
        else:
            try:
                coffee_type = MENU[coffee]

            except KeyError:
                print("Sorry, but this doesn't make that.")
                main()

            stuff = functions.deductor(coffee)
            if stuff == False:
                print("Not enough resources")
            else:
                try:
                    print(f"Please insert coins. Cost: (${MENU[coffee]["cost"]}0)")
                    toonies = int(input("How many Toonies ($2): ").strip())
                    loonies = int(input("How many Loonies ($1): ").strip())
                    quarters = int(input("How many Quarters ($0.25): ").strip())
                    dimes = int(input("How manu Dimes ($0.10): ").strip())
                    nickels = int(input("How many Nickels ($0.05): ").strip())

                except ValueError:
                    print("Sorry, that's not a valid answer")
                    main()

                change = functions.money_converter(toonies, loonies, quarters, dimes, nickels, coffee)

                if change < 0:
                    print("Not enough money. Your money has been refunded.")
                    functions.adder(coffee)
                else:
                    if change != 0:
                        print(f"Your change of ${change:.2f} has been refunded")
                    print(stuff, "☕ Enjoy!!!")

main()


