DOM Node List
========================
A NodeList is a collection of nodes, returned by methods like getElementsByTagName. You can loop through a NodeList to access individual nodes.

Example:

    .. code-block:: javascript
  
        var books = xmlDoc.getElementsByTagName("book");
        for (var i = 0; i < books.length; i++) {
            console.log(books[i].getElementsByTagName("title")[0].childNodes[0].nodeValue);
        }
