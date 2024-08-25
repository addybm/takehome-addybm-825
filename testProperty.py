# testProperty.py
# Addison Mirliani
# Take-home assignment
# 8/25/24

from property import Property

# testing initialization of a property
def testInitProperty():
    prop1 = Property("id_ex_1",["url1","url2"])
    assert(prop1.id == "id_ex_1")
    assert(prop1.images == ["url1","url2"])
    
    # exception-raising (uncomment to run, all have passed):
    
    # should raise exception because id is not a string
    # prop2 = Property(3278,["url1","url2"])
    
    # should raise exception because images is not a list of strings
    # prop3 = Property("id_ex_1",43243)
    # prop4 = Property("id_ex_1",[3,4])
    # prop5 = Property("id_ex_1",["djskl",4])
    
    # raises exception because of incorrect number of arguments
    # prop6 = Property()
    # prop7 = Property(32)

# test getThumbnail function
def testGetThumbnail():
    prop1 = Property("id_ex_1",["url1","url2"])
    assert(prop1.getThumbnail() == "url1")
    prop2 = Property("id_ex_2",[])
    assert(prop2.getThumbnail() == "")

# test getImages function
def testGetImages():
    prop1 = Property("id_ex_1",["url1","url2"])
    assert(prop1.getImages() == ["url1","url2"])
    prop2 = Property("id_ex_2",[])
    assert(prop2.getImages() == [])
    
# test moveImage function
def testMoveImage():
    prop1 = Property("id_ex_1",["url1","url2"])
    # should raise error, uncomment to test
    # prop1.moveImage(0,"1")
    # prop1.moveImage("0",1)
    
    prop1.moveImage(0,1)
    assert(prop1.images == ["url2","url1"])
    prop1.moveImage(0,0)
    assert(prop1.images == ["url2","url1"])
    
    # should raise error, uncomment to test
    # prop2 = Property("id_ex_1", [])
    # prop2.moveImage(0,0)
    
    # should raise error, uncomment to test
    # prop3 = Property("id_ex_1",["url1","url2"])
    # prop3.moveImage(-1,0)
    # prop3.moveImage(0,2)
    # prop3.moveImage(1,-1)
    
    prop4 = Property("id_ex_2",["url1","url2","url3","url4"])
    prop4.moveImage(1,2)
    assert(prop4.images == ["url1","url3","url2","url4"])
    prop4.moveImage(0,3)
    assert(prop4.images == ["url3","url2","url4","url1"])

def main():
    testInitProperty()
    testGetThumbnail()
    testGetImages()
    testMoveImage()
    
if __name__ == "__main__":
    main()
