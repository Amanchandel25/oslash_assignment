from sys import argv
import inventory, messeges, vendor

def main():

    # check if the input file is provided
    if len(argv) != 2:
        raise Exception(messeges.filePathError)
    
    # open the input file and processing the lines
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()

    # initialize the inventory
    localInventory = inventory.inventory(vendor.InventoryList)


    # printing the final bill
    print(localInventory.generateBill(lines))  

if __name__ == "__main__":
    main()
