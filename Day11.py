# TODAY I MADE A MINI PROJECT OF CAFE INVENTORY. 

inventory=[]
while True:
    print("\n********* WELCOME TO MY CAFE 🧋🥤🍷☕🍰🍩🍥 **********")
    print("1.view Inventory: 👀")
    print("2.Add Item: ➕📢")
    print("3.Remove Item: ⛳")
    print("4.Total cafe Inventory: ")
    print("5.Sort Inventory: ")
    print("6.Update Item:" )
    print("7.Search Item: ")
    print("8.Exit........")

    choice=input("Please Enter your choice between 1 to 6: ")

#VIEW INVENTORY

    if choice=="1":
      if not inventory:
        print("Inventory is empty. ")
      else:
        print("\n***** Cafe Invontery☕🍩 *****")
        for item in inventory:
           print(f"Item: {item[0]}| Price: RS {item[1]} | Stock: {item[2]} ")

#ADD ITEM

    elif choice=="2":
       name=input("Enter Item name: ")
       price=float(input("Enter Price : "))
       quantity=int(input("Enter Quantity: "))

       new_product=[name,price,quantity]
       inventory.append(new_product) 
       print("Item added successfully. ")

#REMOVE ITEM

    elif choice=="3":
       remove_name=input("Enter item name to remove :")
       found=False

       for item in inventory:
          if item[0].lower()== remove_name.lower():
             inventory.remove(item)
             print("Item is removed successfuly!!!!")
             found=True
             break
          
       if not found:
          print("Item is not Found.")     

     # TOTA CAFE INVONTORY
             
    elif choice=="4":
       total_value=0
        
       for item in inventory:
          item_value=item[1]*item[2] 
          total_value+=item_value

       print(f"Total cafe value: {total_value}.")  
    
    #SORT INVONTORY

    elif choice=="5":
       inventory.sort()
       print("Inventory is Sorted Alphabatically. ")

       for item in inventory:
           print(f"Item: {item[0]}| Price: RS {item[1]} | Stock: {item[2]} ")
      
      #UPDATE ITEM

    elif choice=="6":
       update_name=input("Enter item name to update: ")
       found=False

       for item in inventory:
          if item[0].lower()==update_name.lower():
             print("Item fond......!! Enter new details.")

             new_price=float(input("Enter new Price : "))
             new_quantity=int(input("Enter quantity: "))

             item[1]= new_price
             item[2]=new_quantity

             print("Item update Successfully!!!!!")
             found=True
             break
          
          if not found:
             print("Item is not found.")

       #SEARCH ITEM
    elif choice=="7":
       search_name=input("Enter item name for search: ")
       found=False

       for item in inventory:
          if item[0].lower()==search_name.lower():
             print("\nItem is found.😊")
             print(f"name: {item[0]} | Price : Rs.{item[1]} | Stock : {item[2]}")
             found=True
             break
          
          if not found:
             print("Item is not found.....😟 ")

    #EXIT

    elif choice=="8":
       print("Closing Cafe System. GOOD BYE 🙌")   
       break

    
    else:
       print("Invalid choice. Please try again.")
  

  
