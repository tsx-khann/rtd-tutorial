XSLT Apply
==========

The `<apply>` element in XSLT is used to **apply a template** to a selected node or nodes.

**Example:** Using `<apply>`

**1. XML Document (input.xml)**

.. code-block:: xml

    <bookstore>
        <book>
            <title>Learn XSLT</title>
            <price>35</price>
        </book>
    </bookstore>

**2. XSLT Stylesheet (transform.xsl)**

.. code-block:: xml

    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="/bookstore">
            <html>
                <body>
                    <h2>Books List</h2>
                    <ul>
                        <xsl:apply-templates select="book"/>
                    </ul>
                </body>
            </html>
        </xsl:template>

        <xsl:template match="book">
            <li>
                <xsl:value-of select="title"/>
            </li>
        </xsl:template>
    </xsl:stylesheet>

**How `<apply>` Works**

- **Applies templates** to selected nodes.
- **Allows for recursive processing** of child nodes.
