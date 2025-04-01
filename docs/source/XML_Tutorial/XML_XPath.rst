XML XPath
=========
XPath is a language for navigating and selecting parts of an XML document. It is often used in conjunction with XML parsers.

Example of using XPath:

.. code-block:: javascript

   var result = xmlDoc.evaluate("//book/title", xmlDoc, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
   console.log(result.singleNodeValue.textContent);
