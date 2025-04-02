XPath Introduction
=================

XPath (XML Path Language) is a language used to **navigate and query XML documents**. It allows you to select nodes and values in an XML document.


**Example:** Select an Element

**1. JavaScript (Using XPath)**

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

---

**What Does XPath Do?**
- **Navigates XML documents** using paths.
- **Queries data** from XML with conditions.
- **Helps in extracting values** or nodes from complex XML structures.
