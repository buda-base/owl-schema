## Modified version of dottoxml

Protégé includes the OntoGraf plugin that allows to create a visual graph display from an ontology and to export that display as a `.dot` format file.

`dottoxml` converts [GraphWiz](http://www.graphviz.org) `.dot` files to `.graphml` files that can be read by [yEd](http://www.yworks.com/products/yed#).

yEd provides reasonable features for cleaning up the graphical display which is tedious and intractable for large graphs in OntoGraf.

The modifications made to dottoxml include:

 - setting arrowheads on the target end of edges; 
 - setting the shape of nodes to ellipse rather than rectangle; 
 - deleting a useless comment about domain and range on edge labels that OntoGraf seems to insert when generating the edge labels from property names'; and 
 - setting the edge style to smooth Bezier rather than PolyLine

Running the dottoxml is done via:

    python dottoxml input-file.dot output-file.graphml

Then open the graphml file in yEd and then select `Tools >> Fit Node to Label` followed by selecting an automatic layout via the `Layout` menu -- the `One-click Layout` works decently.

The [original](https://bitbucket.org/dirkbaechle/dottoxml/get/e285fccba8d5.zip) was downloaded from the [bitbucket](https://bitbucket.org/dirkbaechle/dottoxml) pages [referred to](http://dl9obn.darc.de/programming/python/dottoxml/) from the pages of Dirk Baechle