XML DOM
========

The Document Object Model (DOM) is a programming interface for XML documents. It represents the structure of the document as a tree, where each node is an object representing a part of the document.

Example:

.. code-block:: javascript

   var xmlDoc = parser.parseFromString(xmlString, "text/xml");
   var bookTitle = xmlDoc.getElementsByTagName("title")[0].childNodes[0].nodeValue;
   console.log(bookTitle);
