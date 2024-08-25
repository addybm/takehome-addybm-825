# testPropertyAPI.py
# Addison Mirliani
# Take-home assignment
# 8/25/24

from propertyAPI import PropertyAPI
from property import Property

# Test initialization of property API
def testAPIInit():
    props = PropertyAPI([])
    props2 = PropertyAPI([Property("id",["img"])])
    
    # uncomment to see exception raised
    # props3 = PropertyAPI(["testing"])
    
# test retrieval of list of properties
def testGetBrowseProperties():
    props = PropertyAPI([Property("id_test",["img"])])
    assert(props.getBrowseProperties()[0].id == "id_test")
    
    props2 = PropertyAPI([Property("id_test",["img"]),
    Property("id_test_2",["img,img2"])])
    assert(props2.getBrowseProperties()[0].id == "id_test")
    assert(props2.getBrowseProperties()[1].id == "id_test_2")

# test getting images in order for a specific property
def testGetPropertyImages():
    props = PropertyAPI([Property("id_test",["img"]),
    Property("id_test_2",["img","img2"])])
    assert(props.getPropertyImages("id_test") == ["img"])
    assert(props.getPropertyImages("id_test_2") == ["img","img2"])
    
    # uncomment to see error raised
    # props.getPropertyImages("jdfksl")

# test modifying image order
def testModifyImageOrder():
    props = PropertyAPI([Property("id_test",["img"]),
    Property("id_test_2",["img","img2"])])
    
    # uncomment to see error raised
    # props.modifyImageOrder("fdjksl",0,1)

    assert(props.getPropertyImages("id_test_2") == ["img","img2"])
    props.modifyImageOrder("id_test_2",0,1)
    assert(props.getPropertyImages("id_test_2") == ["img2","img"])
    
    # uncomment to see error raised
    # props.modifyImageOrder("id_test_2",0,2)
    

def main():
    testAPIInit()
    testGetBrowseProperties()
    testGetPropertyImages()
    testModifyImageOrder()
    
if __name__ == "__main__":
    main()
