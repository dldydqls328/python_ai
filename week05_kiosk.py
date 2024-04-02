# ISHS CAFE
# 아메리카노 1500, 라떼 2500

beverage = ["Americano", "Latte"]
price = [1500, 2500]

while True:
    menu = int(input("1) Americano  2) Latte   3) End order : "))
    if menu == 3:
        print("Exit program")
        break
    elif menu == 1:
        print("you ordered Americano coffe. The price is 1,500 won.")
    elif menu == 2:
        print("you ordered a cafe latte. The price is 2,500 won.")
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu.")