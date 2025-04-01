DOM Get Values
========================
To retrieve values from XML nodes, you use methods like getAttribute or textContent.

Example:

    .. code-block:: javascript

        var bookTitle = bookNode.getElementsByTagName("title")[0].textContent;
