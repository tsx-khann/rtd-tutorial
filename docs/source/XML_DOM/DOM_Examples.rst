DOM Examples
========================
Here are some additional examples that demonstrate various XML DOM features, such as creating, accessing, and modifying XML nodes.

Example:

    .. code-block:: javascript
  
        var xmlDoc = parser.parseFromString(xmlString, "text/xml");
        var book = xmlDoc.getElementsByTagName("book")[0];
        var title = book.getElementsByTagName("title")[0].textContent;
        console.log(title);  // Output: Book Title
