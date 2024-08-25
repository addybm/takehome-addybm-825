# propertyAPI.py
# Addison Mirliani
# Take-home assignment
# 8/25/24

from property import Property

class PropertyAPI:
    
    # properties must be a list of Property objects
    def __init__(self,properties : list[Property]):
        # store properties in a dictionary
        self.properties = {}
        for prop in properties:
            if (not isinstance(prop,Property)):
                raise Exception("error: must provide a list of Properties")
            else:
                self.properties[(prop.id)] = prop
                
    # display propertyAPI as a string
    def printProperties(self):
        for key,value in self.properties.items():
            print(value)
            print()

    # Purpose    : return list of properties
    # Parameters : self
    # Returns    : return list of properties
    def getBrowseProperties(self):
        browseList = []
        for key,value in self.properties.items():
            browseList.append(value)
        return browseList
        
    # Purpose    : given a property ID, return the images in the correct order
    #              for that property
    # Parameters : self
    #              property ID - string
    # Returns    : list of image urls in the correct order
    # Exceptions : raises exception if given id is not present in list of
    #              properties
    def getPropertyImages(self,id : str):
        # check if key is present in dictionary
        if (not id in self.properties.keys()):
            raise Exception("error: id not present in properties")
        
        return self.properties[id].getImages()
    
    
    # Purpose    : allow users to change the order of images given a property id
    # Parameters : property ID - string
    #              start       - integer, initial list position of image to move
    #              end         - integer, ending list position of image to move
    # Returns    : none
    # Exceptions : raises exception if given id is not present in list of
    #              properties
    def modifyImageOrder(self,id : str, start : int, end : int):
        # check if key is present in dictionary
        if (not id in self.properties.keys()):
            raise Exception("error: id not present in properties")
            
        self.properties[id].moveImage(start,end)
        
