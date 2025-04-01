DOM Replace Nodes
========================
Replace nodes using the replaceChild method.

Example:

    .. code-block:: javascript
  
        var newNode = document.createElement("book");
        var oldNode = document.getElementsByTagName("book")[0];
        parent.replaceChild(newNode, oldNode);
