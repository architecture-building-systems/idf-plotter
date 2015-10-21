'''
findreferences.py

create a graph of the (named) objects in an idf file.
the output is in DOT, so it can be visualized with graphviz.
'''
import parseidf
import re

def print_dot(idf, names):
    '''
    idf is the output of parseidf.parse(string).
    '''
    objects = get_objects(idf) 
    print 'digraph G {'
    print '\toverlap = false'
    for o in (o for o in objects if o[1] in names):
        # backlinks
        for other in objects:
            if other == o:
                continue
            for v in other[2:]:
                if v == o[1]:
                    print '\t"%s %s" -> "%s %s"' % (other[0], other[1], o[0], o[1])
    print '}'

def get_objects(idf):
    return [o for sublist in idf.values() for o in sublist]

def print_names(idf):
    objects = get_objects(idf)
    names = ['%s;%s' % (o[0].strip(), o[1].strip()) for o in objects if len(o) > 1 and o[1].strip() != '' and not is_number(o[1])]
    for n in sorted(names):
        print n

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-i', '--idf', dest='idf')
    parser.add_option('-n', '--names', dest='names')
    options, args = parser.parse_args()

    idf = parseidf.parse(open(options.idf, 'r').read())

    if options.names:
        names = [n[n.find(';') + 1:].strip() for n in open(options.names, 'r').readlines()]
        print_dot(idf, names) 
    else:
        print_names(idf)
