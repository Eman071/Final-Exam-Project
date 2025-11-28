# /C:/Users/hp/Desktop/Final Exam/Backend/main.py
def greeting(name):
   
    print("Hello " + name + ", welcome to our Shop. \n")

user = input("What's your name? \n")

greeting(user)
print("-" * 20)
# -------------------------/

products = [
    ["Table"],
    ["Chair"],
    ["Lamp"],
    ["Sofa"],
    ["Bed"],
]
print("Available products:\n")
for i, (name) in enumerate(products, start=1):
    print(f"{i}. {name[0]}")
print("-" * 20)


def main(): 
    products = [
        ["Table", 1200],
        ["Chair", 600],
        ["Lamp", 250],
        ["Sofa", 2000],
        ["Bed", 1800],
    ]

    try:
        user_choice = int(input("Enter product number: "))

        if 1 <= user_choice <= len(products):
            name, price = products[user_choice - 1]
            tax_rate = 0.15
            price_with_tax = price + (price * tax_rate)

        else:
            print("Error: Invalid number entered. Please select a number from the list.")
            return
    except (ValueError, EOFError):
        print("Error: please enter a valid number.")
        return

   
    
    print(f"{name} price including tax ({tax_rate*100:.0f}%): {price_with_tax:.2f}")

if __name__ == "__main__":

  main() 

print("-" * 20)
print("Thank you for visiting our Shop. Have a great day!")
input("Press Enter to exit...")
