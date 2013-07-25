def qname(ns,t):
    o={}
    for x in t.split(','):
        o.update({x: ns + x})
    return o


