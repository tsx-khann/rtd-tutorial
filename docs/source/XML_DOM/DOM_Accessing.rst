DOM Accessing
=================
You can access XML DOM nodes using various methods like getElementById, getElementsByTagName, getElementsByClassName, etc.

Example:

  .. code-block:: javascript
  
    var xmlDoc = parser.parseFromString(xmlString, "text/xml");
    var books = xmlDoc.getElementsByTagName("book");
