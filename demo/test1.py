from pprint import pprint
import sys
import time
import ConfigParser

sys.path.append('..')
import pygento

__author__ = 'roberto'


def arrichisce(conn, cat_tree):
    childs = []
    for children in cat_tree['children']:
        childs.append(arrichisce(conn, children))
    data = conn.infoCategory(cat_tree['category_id'])
    cat_tree.update(data)
    cat_tree['children'] = childs
    return cat_tree


if __name__ == "__main__":
    config = ConfigParser.ConfigParser()
    config.read(sys.argv[1])
    conn = pygento.Magento(
        config.get('General', 'url', ''),
        config.get('General', 'user', ''),
        config.get('General', 'pass', '')
    )

    prodotto = conn.getProductInfo('573600')
    del prodotto['price']
    pprint(prodotto)
    pprint(conn.listProducts({'name': {'like': '%robot%'}})[:2])

    starttime = time.time()
    cat_tree = conn.treeCategory(1)
    print "Api categorie in ", time.time() - starttime
    print "Arricchimento..."
    starttime = time.time()
    arrichisce(conn, cat_tree)
    print "Arricchimento categorie in ", time.time() - starttime
    pprint(cat_tree)
