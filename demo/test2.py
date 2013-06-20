from pprint import pprint
import sys
import time
import ConfigParser

sys.path.append('..')
import pygento

__author__ = 'roberto'

if __name__ == "__main__":
    config = ConfigParser.ConfigParser()
    config.read(sys.argv[1])
    conn = pygento.Magento(
        config.get('General', 'url', ''),
        config.get('General', 'user', ''),
        config.get('General', 'pass', '')
    )

    starttime = time.time()
    cat_tree = conn.treeCategoryFull(1)
    print "conn.treeCategoryFull(1) in ", time.time() - starttime
    pprint(cat_tree)
