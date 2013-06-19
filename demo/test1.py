from pprint import pprint
import sys

sys.path.append('..')
import pygento
import ConfigParser

__author__ = 'roberto'

if __name__ == "__main__":
    config = ConfigParser.ConfigParser()
    config.read(sys.argv[1])
    conn = pygento.Magento(
        config.get('General', 'url', ''),
        config.get('General', 'user', ''),
        config.get('General', 'pass', '')
    )
    pprint(conn.treeCategory(1))
    prodotto = conn.getProductInfo('573600')
    del prodotto['price']
    pprint(prodotto)
    pprint(conn.listProducts({'name': {'like': '%robot%'}}))
