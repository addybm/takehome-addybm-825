# property.py
# Addison Mirliani
# Take-home assignment
# 8/25/24

class Property:
    
    # Property id must be a string
    # Property images must be a list of strings (url)
    # if these criteria are not met, an exception will be raised
    def __init__(self,id : str,images : list[str]):
        if (isinstance(id,str)):
            self.id = id
        else:
            raise Exception("error: given ID is not a string")
        
        if (not isinstance(images,list)):
            raise Exception("error: given images are not a list")
        for img in images:
            if (not isinstance(img,str)):
                raise Exception("error: given image is not a string")
        self.images = images
        
    # Purpose    : returns thumbnail image
    # Parameters : self
    # Returns    : URL of thumbnail image
    def getThumbnail(self):
        # if there are no images, return an empty string
        if (len(self.images) == 0):
            return ""
        else:
            return self.images[0]
    
    # Purpose    : returns images in order
    # Parameters : self
    # Returns    : list of images in order
    def getImages(self):
        return self.images
    
    # Purpose    : re-orders images
    # Parameters : self
    #              start - integer starting position of image to move
    #              end   - integer ending position of image to move
    # Returns    : none
    # Exceptions : raises exception if start or end are out of bounds of
    #              the images list or if they are not integers
    def moveImage(self,start : int, end : int):
        # check that all parameters are valid
        if (len(self.images) == 0):
            raise Exception("error: cannot move images in empty list")
        if ((not isinstance(start,int)) or (not isinstance(end,int))):
            raise Exception("error: start and end must be integers")
        if ((start < 0) or (start > len(self.images) - 1) or (end < 0) or
            (end > len(self.images) - 1)):
            raise Exception("error: start and end must be within the bounds of"
            " the list")
            
        
            
