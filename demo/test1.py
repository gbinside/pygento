from pprint import pprint
import sys

sys.path.append('..')
import pygento

__author__ = 'roberto'

if __name__ == "__main__":
    conn = pygento.Magento('http://terminalvideo.local/index.php/api/xmlrpc/', 'python', 'password')
    pprint(conn.treeCategory(1))
    prodotto = conn.getProductInfo('573600')
    del prodotto['price']
    pprint(prodotto)
    pprint(conn.listProducts({'name': {'like': '%robot%'}}))
