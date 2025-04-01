XML DOM Nodes
=============

In the XML DOM, the document is represented as a tree of nodes. Each node can represent different parts of the XML document.

**Types of Nodes:**
- **Document Node:** Represents the entire XML document.
- **Element Nodes:** Represent XML elements (e.g., `<book>`, `<author>`).
- **Attribute Nodes:** Represent attributes of elements (e.g., `category="fiction"`).
- **Text Nodes:** Contain the text content within elements.
- **Comment Nodes:** Represent comments within the XML document.

Example XML Document:
```xml
<?xml version="1.0"?>
<bookstore>
    <book category="cooking">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>
    <book category="children">
        <title lang="en">Harry Potter</title>
        <author>J.K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
</bookstore>
