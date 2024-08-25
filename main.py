# main.py
# Addison Mirliani
# Take-home assignment
# 8/25/24

import json
from propertyAPI import PropertyAPI
from property import Property

# Purpose    : reads from database.json and creates an instance of propertyAPI
# Parameters : none
# Returns    : instance of propertyAPI
def readProperties():
    # open JSON file
    file = open("database.json")

    # load data from "database"
    data = json.load(file)
    
    # close file
    file.close()

    # create list of properties
    properties = []
    for property in data["properties"]:
        properties.append(Property(property["id"],property["images"]))
    
    return PropertyAPI(properties)
    

def main():
    
    properties = readProperties()
    print("Welcome! Here are your current properties:")
    properties.printProperties()
    
    action = ""
    while (not action == "q"):
        # getBrowseProperties
        # getPropertyImages
        # modifyImageOrder
        action = input("please type b (browse list of properties), i "
        "(get images for a specific property), "
        "m (modify image order for a specific property), or q (quit): ")
        
        if (action == "b"):
            browseProperties = properties.getBrowseProperties()
            for prop in browseProperties:
                print(prop)
        elif (action == "i"):
            propID = input("please input the id of the property whose images"
            " you would like to view: ")
            print(properties.getPropertyImages(propID))
        elif (action == "m"):
            propID = input("please input the id of the property whose image"
            " order you would like to modify: ")
            start = int(input("input the starting position of the image you"
            " would like to move: "))
            end = int(input("input the ending position of the image you would"
            " like to move: "))
            properties.modifyImageOrder(propID,start,end)
        elif (action == "q"):
            # TODO: save info
            print("Thank you!")
        else:
            print("error: please choose a correct option")
        
    #if (action == "q"):
        # TODO: save info
    
    
if __name__ == "__main__":
    main()
