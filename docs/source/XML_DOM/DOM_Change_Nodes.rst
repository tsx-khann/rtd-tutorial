DOM Change Nodes
========================
You can modify nodes using methods like setAttribute, appendChild, and replaceChild to alter the content or structure of the document.

Example:

    .. code-block:: javascript
  
        var titleNode = bookNode.getElementsByTagName("title")[0];
        titleNode.textContent = "Updated Title";
