XSLT <if>
=========

The `<if>` element in XSLT allows you to **conditionally process** nodes based on an expression or condition.



**Example:** Using `<if>`

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
                            <xsl:if test="price > 30">
                                <li>
                                    <xsl:value-of select="title"/>
                                </li>
                            </xsl:if>
                        </xsl:for-each>
                    </ul>
                </body>
            </html>
        </xsl:template>
    </xsl:stylesheet>



**How `<if>` Works**

- **Applies conditions** before transforming nodes.
- **Processes nodes based on a test condition**.
