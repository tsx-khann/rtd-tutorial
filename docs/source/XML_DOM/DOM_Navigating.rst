DOM Navigating
========================
Navigating through the XML DOM allows you to access related nodes. You can use properties like nextSibling, previousSibling, and parentNode to move between nodes.

Example:

    .. code-block:: javascript
  
        var bookNode = document.getElementsByTagName("book")[0];
        var nextBook = bookNode.nextSibling;
