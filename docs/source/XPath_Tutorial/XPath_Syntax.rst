XPath Syntax
============

XPath syntax defines how you **select nodes** in an XML document. It uses **path expressions** to navigate the XML tree structure.


**Example:** Basic XPath Syntax

**1. JavaScript (XPath Query)**

.. code-block:: javascript

    var xmlDoc = document.getElementById("myXML");
    var result = xmlDoc.evaluate("/bookstore/book/title", xmlDoc, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
    var node = result.singleNodeValue;
    alert(node.childNodes[0].nodeValue);

**2. XML File (myXML.xml)**

.. code-block:: xml

    <bookstore>
      <book>
        <title>Learn XPath</title>
      </book>
    </bookstore>


**Basic XPath Syntax**

- **Node Selection**: `/` denotes the root, `//` searches anywhere in the document.
- **Attributes**: `@` is used to select attributes (`/bookstore/book/@id`).
- **Predicates**: `[]` to filter nodes (`/bookstore/book[1]`).
