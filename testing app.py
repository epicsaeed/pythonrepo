


with open('inventory_updated.txt','r+') as f:
    inventorynew = list(f)

with open('inventory.txt','r+') as f:
    inventory = list(f)

print("old inv",inventory,"\n\n\n")
print("new inv",inventorynew)



    # print("Items added in the last run:\n")
    # #print("ProductID\tName\t\tSize\tColor\tinStock")
    # #print('_'*60)

    # c = 0
    # while c < len(added):
    #     if added[c] in productID:
    #         print(added[c],"\t",name[c].ljust(15),size[c],"\t",color[c],"\t",inStock[c])
    #     c+=1

    # print("Items deleted in the last run:\n")
    # #print("ProductID\tName\t\tSize\tColor\tinStock")
    # #print('_'*60)
    # c = 0
    # while c < len(deleted):
    #     if deleted[c] in productID:
    #         print(deleted[c],"\t",name[c].ljust(15),size[c],"\t",color[c],"\t",inStock[c])
    #     c+=1