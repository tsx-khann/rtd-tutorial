XPath Axes
==========

XPath axes define the **relationship between nodes** in the document. They help identify the context of a node relative to others.


**Example:** Using an XPath Axis

**1. JavaScript (XPath Axis Example)**
.. code-block:: javascript

    var xmlDoc = document.getElementById("myXML");
    var result = xmlDoc.evaluate("/bookstore/book/title/parent::*", xmlDoc, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
    var node = result.singleNodeValue;
    alert(node.nodeName);

**2. XML File (myXML.xml)**

.. code-block:: xml

    <bookstore>
      <book>
        <title>Learn XPath</title>
      </book>
    </bookstore>


**Common XPath Axes**

- **child**: Selects children of the current node.
- **parent**: Selects the parent node.
- **following-sibling**: Selects nodes after the current one.
