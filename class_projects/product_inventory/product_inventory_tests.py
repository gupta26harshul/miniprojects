'''
Created on 11/07/2013

@author: luke

Product Inventory Project – Create an application which manages
an inventory of products. Create a product class which 
has a price, id, and quantity on hand. Then create an 
inventory class which keeps track of various products and 
can sum up the inventory value.
'''
import unittest
import product_inventory 
from product_inventory import Product

class TestInventory(unittest.TestCase):
    """
        an inventory contains {0,infinity} products.
        each inventory has a list of the products it has
        that lists the amount of product and connects to the actual product
        each inventory can sum up the products it has to list the total amount
    """
    def setUp(self):
        self.inv    = product_inventory.Inventory()
        
    def tearDown(self): 
        del self.inv
        
    def testAddCountProduct(self):
        """
        count_product returns the amount of products in the inventory
            add_product can take multiple products as an argument and will add them all.
            add_product can take lists of products, or any sequence, as arguments and add them all
        """
        product = (apple, orange,banana) = Product(name="apple"), Product(name="orange"), Product(name="banana")
        self.inv.product_add(product)
        count   = self.inv.product_count()
        self.assertEqual(count,3,"Expected 3 for product count, got {0}".format(count))
        self.inv.product_add(apple, orange)
        count   = self.inv.product_count()
        self.assertEqual(count,5,"Expected 5 for product count, got {0}".format(count))
        
    def testID(self):
        """
            It's expected each inventory will have a unique identifier
        """
        inv     = product_inventory.Inventory
        curr    = inv()
        for i in range(5):
            next = inv()
            self.assertEqual(curr.id+1, next.id, "ID change not as expected")
            curr = next
        
        
        

class TestInventoryFactory(unittest.TestCase):
    """
        An Inventory Factory should be able to generate
        an inventory. Each inventory should have a unique
        identifier
    """
    def setUp(self):
        self.inv_factory    = product_inventory.InventoryFactory()
        
    def testGetObject(self):
        """
            get_object is expected to return a new inventory
            get_object will return the amount of objects that is passed in as an arg
        """
        invs                = (inventory, second_inv) = self.inv_factory.get_object(2)
        cls                 = product_inventory.Inventory
        # an inv factory should produces unique inventories
        for inv in invs:
            self.assertIsInstance(inv, cls, "{0} is not instance of {1}".format(inv, cls))
        self.assertNotEqual(invs[0], invs[1], "Each inventory should be unique")
            
class TestProductFactory(unittest.TestCase):
    """
        A product factory should generate a product.
        Each product should have a unique identifier
    """
    def setUp(self):
        self.product_factory = product_inventory.ProductFactory()
           
    def testGetObject(self):
        """
            get_object os ex[ected to return a new product
            get_object will return the amount of objects that is passed in as an arg
            each object will be uniquely defined
        """
        products    = self.product_factory.get_object(2)
        cls         = self.product_factory.Product
        for prod in products:
            # check if in correct class and is not equal
            self.assertIsInstance(prod, cls, "{0} is not instance of {1}".format(prod, cls))
        self.assertNotEqual(products[0], products[1], "Each product should be unique")
    
        

class TestProductInventory(unittest.TestCase):
    # Create an Inventory Factory to create Inventories
    # and a Product Factory for Products
    inv_factory             = product_inventory.InventoryFactory()
    prod_factory            = product_inventory.ProductFactory()

    def setUp(self):
        pass

    def tearDown(self):
        # reset inventories and products
        self.inventories    = []
        self.products       = []


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()