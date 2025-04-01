DOM Clone Nodes
========================
Clone nodes using the cloneNode method. This allows you to copy an element and its descendants.

Example:

    .. code-block:: javascript
  
        var clone = bookNode.cloneNode(true); 
        parent.appendChild(clone);
