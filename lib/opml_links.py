
links_list = lambda opml: [x.attrib['xmlUrl'] for x in opml._tree.findall('.//outline[@xmlUrl]')]
