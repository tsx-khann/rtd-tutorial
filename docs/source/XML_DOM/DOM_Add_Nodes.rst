DOM Add Nodes
========================
Add new nodes to the DOM tree using methods like appendChild, insertBefore, and prepend.

Example:

    .. code-block:: javascript
  
        var newNode = document.createElement("author");
        newNode.textContent = "New Author";
        bookNode.appendChild(newNode);
