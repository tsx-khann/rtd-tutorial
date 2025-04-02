XPath Nodes
===========

In XPath, **nodes** are the basic building blocks. They can be **elements, attributes, text** and more. XPath selects and manipulates nodes in an XML document.

**Example:** Select a Node

**1. JavaScript (XPath for Node Selection)**

.. code-block:: javascript

    var xmlDoc = document.getElementById("myXML");
    var result = xmlDoc.evaluate("/bookstore/book/title", xmlDoc, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
    var node = result.singleNodeValue;
    alert(node.nodeName);

**2. XML File (myXML.xml)**

.. code-block:: xml

    <bookstore>
      <book>
        <title>Learn XPath</title>
      </book>
    </bookstore>



**Types of XPath Nodes**

- **Element nodes**: Represent XML elements.
- **Text nodes**: Represent text inside elements.
- **Attribute nodes**: Represent attributes of elements.
