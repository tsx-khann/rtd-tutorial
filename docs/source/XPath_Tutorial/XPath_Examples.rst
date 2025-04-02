XPath Examples
==============

XPath examples demonstrate how to **select specific elements** or **extract values** from an XML document.


**Example 1:** Select All Books

**1. JavaScript (Using XPath)**

.. code-block:: javascript

    var xmlDoc = document.getElementById("myXML");
    var result = xmlDoc.evaluate("//bookstore/book", xmlDoc, null, XPathResult.ANY_TYPE, null);
    var node = result.iterateNext();
    while (node) {
      alert(node.childNodes[0].nodeValue);  // Display book titles
      node = result.iterateNext();
    }

**2. XML File (myXML.xml)**

.. code-block:: xml

    <bookstore>
      <book>
        <title>Learn XPath</title>
      </book>
      <book>
        <title>Mastering XML</title>
      </book>
    </bookstore>


**Example 2:** Select Books with Price Greater Than 30

**1. JavaScript (XPath with Condition)**

.. code-block:: javascript

    var xmlDoc = document.getElementById("myXML");
    var result = xmlDoc.evaluate("/bookstore/book[price>30]", xmlDoc, null, XPathResult.ANY_TYPE, null);
    var node = result.iterateNext();
    alert(node.childNodes[0].nodeValue);  // Display book titles with price > 30

**2. XML File (myXML.xml)**

.. code-block:: xml

    <bookstore>
      <book>
        <title>Learn XPath</title>
        <price>35</price>
      </book>
      <book>
        <title>Mastering XML</title>
        <price>25</price>
      </book>
    </bookstore>


**XPath in Action**

- **Extract specific nodes** using conditions.
- **Filter and compare nodes** with XPath operators.
- **Iterate through results** with JavaScript.
