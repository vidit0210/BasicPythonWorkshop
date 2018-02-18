#Create a billing system adding GST and giving option for Service tax
#List to Hold Item Name
#List to Hold Price
#Show Complate Bill

bill =0
condition = True
item_name = []
price_of_item=[]

while(condition==True):
    item=input("Enter Item Name: \n")
    item_name.append(item)
    amount = float(input("Enter the price : \n"))
    price_of_item.append(amount)
    bill = bill + amount
    prompt=input("Would you like to Continue Shopping?: \n")
    if(prompt=="no"or prompt=="NO"):
        condition=False

tax= (5.6/bill) * 100
bill = bill+tax

service_tax = 50
add_st = input("Would you like to add Service Tax?: \n")
if(add_st=="yes" or add_st =="YES"):
    print(bill+service_tax)
else:
    print(bill)
    print(item_name)
    print(price_of_item)


