from pprint import pprint
import sys
import time
import ConfigParser
import collections

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

    attr_sets = conn.listAttributeSet()
    nm_attr_attr_set = collections.defaultdict(list)
    all_attributes = {}

    for attr_set in attr_sets: 
        print '#'+attr_set['name'].center(78,'*')
        attrs = conn.listAttribute(attr_set['set_id'])
        for attr in attrs:
            nm_attr_attr_set [attr_set['name']].append( attr['code'] )
            if attr['code'] not in all_attributes:
                print '#'+attr['code'].center(70,'-')
                attr_info = conn.infoAttribute(attr['attribute_id'])
                all_attributes[attr['code']] = attr_info
            
    print "attr_sets =",
    pprint(attr_sets)
    print "nm_attr_attr_set =",
    pprint(dict(nm_attr_attr_set))        
    print "all_attributes =",
    pprint(all_attributes)        
