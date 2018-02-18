#Create a billing system adding GST and giving option for Service tax

bill =0
condition = True

while(condition==True):
    amount = float(input("Enter the price : \n"))
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


