XPath Operators
===============

XPath operators are used to **filter or compare nodes**. They include operators like `=`, `!=`, `>`, `<`, and logical operators like `and` and `or`.


**Example:** Using XPath Operators

**1. JavaScript (XPath Operators Example)**

.. code-block:: javascript

    var xmlDoc = document.getElementById("myXML");
    var result = xmlDoc.evaluate("/bookstore/book[price>30]", xmlDoc, null, XPathResult.ANY_TYPE, null);
    var node = result.iterateNext();
    alert(node.childNodes[0].nodeValue);

**2. XML File (myXML.xml)**

.. code-block:: xml

    <bookstore>
      <book>
        <title>Learn XPath</title>
        <price>35</price>
      </book>
    </bookstore>


**Common XPath Operators**

- **`=`**: Equal to.
- **`!=`**: Not equal to.
- **`>`**: Greater than.
- **`<`**: Less than.
- **`and` / `or`**: Logical operators.
