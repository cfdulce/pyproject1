#menu project with calculation of ending balance

print("Welcome to our restaurant!")
print("\n")
print("---MENU ITEMS---")
print("\n")

#menu items
foods={"Spaghetti":11.32,
"Steak":19.98,
"Fajita tacos (2)":7.54,
"Bowl of rice":5.35,
"Lasagna":15.66 
}

drinks={"Coca-Cola":1.35,
"Lemonade":2.54,
"Dr. Pepper":1.67,
"Sweet Tea":2.04,
"Water":1.00}

print("Foods:")
print(foods)
print("\n")
print("Drinks:")
print(drinks)

print("\n")

#ask user what items they will like to purchase
userquestion=[] #foods
itemPrice=[] #prices
total=0 #total
while True:
  question=input("What will you like to order?(type 'e' once finished) ")
  if question=="e":
    break
  else:
    prices=(input("What is the price of this item? $"))
   

print("\n")
#calculate the total of the chose items
print("---TOTALS---")
for userquestion in question:
  print(question) #ASK PROF MOON FOR HELP WITH THIS

for itemsPrice in prices:
  total+=prices

print(f"Total for all items: ${total}")