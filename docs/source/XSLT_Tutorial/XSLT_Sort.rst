XSLT <sort>
===========

The `<sort>` element is used to **sort nodes** in a specified order, such as alphabetical or numeric.



**Example:** Using `<sort>`

**1. XML Document (input.xml)**

.. code-block:: xml

    <bookstore>
        <book>
            <title>Learn XSLT</title>
            <price>35</price>
        </book>
        <book>
            <title>Mastering XML</title>
            <price>25</price>
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
                        <xsl:for-each select="book">
                            <xsl:sort select="price"/>
                            <li>
                                <xsl:value-of select="title"/>
                            </li>
                        </xsl:for-each>
                    </ul>
                </body>
            </html>
        </xsl:template>
    </xsl:stylesheet>



**How `<sort>` Works**

- **Sorts XML nodes** based on a specific criteria (like price).
- **Can be combined with `<for-each>`** to sort within a loop.
