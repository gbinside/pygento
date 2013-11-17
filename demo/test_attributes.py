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
    
    attributes_done = {}

    print 'current store', conn.currentStoreAttribute()
    print 'attribute types ', 
    pprint(conn.typesAttribute())

    starttime = time.time()
    attr_sets = conn.listAttributeSet()
    print "conn.listAttributeSet() in ", time.time() - starttime
    pprint(attr_sets)

    for attr_set in attr_sets: 
        print attr_set['name'].center(80,'*')
        starttime = time.time()
        attrs = conn.listAttribute(attr_set['set_id'])
        print "conn.listAttribute() in ", time.time() - starttime
        for attr in attrs:
            print attr['code'].center(70,'-')
            pprint(attr)
            if attr['code'] not in attributes_done:
                attributes_done[attr['code']] = 1
                starttime = time.time()
                attr_info = conn.infoAttribute(attr['attribute_id'])
                print "conn.infoAttribute() in ", time.time() - starttime
                pprint(attr_info)
            
    
