from qname import qname
import simplejson

ctx = qname("http://opml.org/spec2#","opml,title,outline")

def recurse_outlines(outlines):
        global debugvalue
        processed=[]
        for outline in outlines:
                attributes = dict(outline._root.attrib.items())
                if len(outline._outlines) > 0:
                        new_outlines = recurse_outlines(outline._outlines)
                        attributes.update({"outlines": new_outlines})
                processed.append({"outline": attributes})
        return processed

def jsonld_from_opml(o):
	ld_doc = {"@context": ctx, "opml": recurse_outlines(o._outlines), "title": o._tree.find('head/title').text}
	return simplejson.dumps(ld_doc)
