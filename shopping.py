import prices


print("SPS--> SPICES MLK-->MILK BRD-->BREAD CCN-->CHICKEN PSA-->PASTA FRT-->FRUITS UTS-->UTENSILS POT-->POTS PFS-->PERFUMES CCE-->CHOCOLATE")




item = input("Enter the item you wish to buy with the following codes  ")



if item == "SPS":
    x = prices.SPICES
    print("YOU HAVE SELECTED SPICES")
    quantity = input("Enter the quantity of the item here  ")
    total = int(quantity)*x
    print("The total is :",total)
    

if item == "MLK":
    Y = prices.MILK
    print("YOU HAVE SELECTED MILK")
    quantity = input("Enter the quantity of the item here  ")
    total = int(quantity)*Y
    print("The total is :",total)



if item == "CCN":
    a = prices.CHICKEN
    print("YOU HAVE SELECTED CHICKEN")
    quantity = input("Enter the quantity of the item here  ")
    total = int(quantity)*a
    print("The total is :",total)
    
    

if item == "PSA":
    z = prices.PASTA
    print("YOU HAVE SELECTED PASTA")
    quantity = input("How many do you wish to buy  ")
    total = int(quantity)*z
    print("The total is :",total)  



if item == "FRT":
    c = prices.FRUITS
    print("YOU HAVE SELECTED FRUITS")
    quantity = input("How many do you wish to buy  ")
    total = int(quantity)*c
    print("The total is :",total)
    
    

if item == "UTS":
    s = prices.UTENSILS
    print("YOU HAVE SELECTED UTENSILS")
    quantity = input("How many do you wish to buy  ")
    total = int(quantity)*s
    print("The total is :",total)



if item == "POT":
    t = prices.POTS
    print("YOU HAVE SELECTED POTS")
    quantity = input("How many do you wish to buy  ")
    total = int(quantity)*t
    print("The total is :",total)
    
    

if item == "PFS":
    p = prices.PERFUMES
    print("YOU HAVE SELECTED PERFUMES")
    quantity = input("How mny do you wish to buy")
    total = int(quantity)*p
    print("The total is :",total)    
    


if item == "CCE":
    u = prices.CHOCOLATE
    print("YOU HAVE SELECTED CHOCOLATE")
    quantity = input("How many do you wish to buy ")
    total = int(quantity)*u
    print("The total is :",total)    
    
    
    
