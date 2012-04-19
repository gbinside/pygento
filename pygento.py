import xmlrpclib
import base64

class NotConnected(Exception):
    pass

class MagentoConnection(object):
    def __init__(self, url, username, apikey):
        self.url = url
        self.username = username
        self.apikey = apikey
        self.connect()

    def connect(self):
        '''Connect to Magento's xmlrpc'''
        self.server = xmlrpclib.ServerProxy(self.url)
        self.token = self.server.login(self.username, self.apikey)

    def _call(self, res, *args, **kwargs):
        if not self.token:
            raise NotConnected()
        return self.server.call(self.token, res, *args, **kwargs)

class Magento(MagentoConnection):

    #PRODUCT OPERATIONS
    def listProducts(self, filters=[]):
        '''Retrieve products list by filters'''
        return self._call('catalog_product.list', [filters,])

    def getProductInfo(self, sku):
        '''Gives the product info'''
        return self._call('catalog_product.info', [sku])

    def updateProductData(self, sku, productdata):
        '''Updates the products for the product with the given sku'''
        return self._call('catalog_product.update', [sku, productdata])

    def createProductData(self, product_type, attribute_id, sku, productdata):
        '''Create new product and return product id'''
        return self._call('catalog_product.create', [product_type, attribute_id, sku, productdata])

    def deleteProductData(self, sku):
        '''Delete product'''
        return self._call('catalog_product.delete', [sku,])

    #IMAGE OPERATIONS
    def getImagesOfProducts(self, sku):
        '''Retrieves all images of a product'''
        return self._call('catalog_product_attribute_media.list', [sku])

    def updateImageOfProducts(self, sku, image_location, image_data):
        '''Update image data of a image'''
        return self._call('catalog_product_attribute_media.update', [sku, image_location, image_data])

    def removeImageOfProduct(self, sku, image_location):
        '''Remove a image of a product'''
        return self._call('catalog_product_attribute_media.remove', [sku, image_location])

    def addImageToProduct(self, sku, image_path, exclude=False, position=0, types=[]):
        '''Adds an image to a product'''
        image_file = open(image_path, "rb")
        encoded_string = base64.b64encode(image_file.read())
        image_data = {'exclude': exclude,
                      'position': position,
                      'types': types,
                      'file': {'content': encoded_string, 
                               'mime': 'image/jpeg'}}
        return self._call('catalog_product_attribute_media.create', [sku, image_data])

    #CATEGORY OPERARTIONS
    def currentStore(self, store_view):
        '''Set/Get current store view'''
        return self._call('catalog_category.currentStore', [store_view,])

    def createCategory(self, parent_category_id, categorydata):
        '''Create a category'''
        return self._call('catalog_category.create', [parent_category_id, categorydata])

    def assignProduct(self, category_id, product_sku):
        '''Assign a product to a category'''
        return self._call('catalog_category.assignProduct', [category_id, product_sku])

    def updateCategory(self, category_id, categorydata):
        '''Update a category'''
        return self._call('catalog_category.update', [category_id, categorydata])

    def moveCategory(self, category_id, parent_id):
        '''Move category into another category'''
        return self._call('catalog_category.move', [category_id, parent_id])

    def treeCategory(self, parent_id):
        '''Retrieve category tree'''
        return self._call('catalog_category.tree', [parent_id,])

    def assignedProducts(self, category_id, store_id):
        '''Retrieve all assigned products'''
        return self._call('catalog_category.assignedProducts', [category_id, store_id])

    def infoCategory(self, category_id):
        '''Retrieve category data'''
        return self._call('catalog_category.info', [category_id,])

    #PRODUCT LINK
    def listProductLink(self, link_type, sku):
        '''Retrieve linked products '''
        return self._call('product_link.list', [link_type, sku])

    def assignProductLink(self, link_type, sku, sku2, link_data=[]):
        '''Assign product link '''
        return self._call('product_link.assign', [link_type, sku, sku2, link_data])

    #ATTRIBUTE OPERARTIONS
    def listAttributeSet(self):
        '''Retrieve product attribute sets'''
        return self._call('product_attribute_set.list')

    def listAttribute(self, attribute_id):
        '''Retrieve attribute list'''
        return self._call('product_attribute.list', [attribute_id,])

    def getAttributeOptions(self, attribute_id):
        '''Retrieve attribute options'''
        return self._call('product_attribute.options', [attribute_id,])

    #PRODUCT STOCK
    def listProductStock(self, sku):
        '''Retrieve stock data by product ids'''
        return self._call('product_stock.list', [sku,])

    def updateProductStock(self, sku, stockdata):
        '''Update product stock data''' 
        return self._call('product_stock.update', [sku, stockdata])

    #SALES ORDER
    def listSalesOrder(self, filters = []):
        '''Retrieve list of orders by filters '''
        return self._call('sales_order.list', [filters,])

    def infoSalesOrder(self, increment_id):
        '''Retrieve order information'''
        return self._call('sales_order.info', [increment_id,])

if __name__ == "__main__":
    MAGENTO_XMLRPC_URL = 'http://www.yourmagento.com/index.php/api/xmlrpc/'

    magento = Magento(url=MAGENTO_XMLRPC_URL, 
                      username="username", 
                      apikey="apikey")
