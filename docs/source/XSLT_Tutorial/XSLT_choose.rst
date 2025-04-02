XSLT <choose>
=============

The `<choose>` element in XSLT provides a way to **select between different conditions**. It is used to create **multiple conditional tests** similar to a switch or if-else statement.

**Example:** Using `<choose>`

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
                            <xsl:choose>
                                <xsl:when test="price > 30">
                                    <li>
                                        <xsl:value-of select="title"/> - Expensive
                                    </li>
                                </xsl:when>
                                <xsl:otherwise>
                                    <li>
                                        <xsl:value-of select="title"/> - Affordable
                                    </li>
                                </xsl:otherwise>
                            </xsl:choose>
                        </xsl:for-each>
                    </ul>
                </body>
            </html>
        </xsl:template>
    </xsl:stylesheet>

**How `<choose>` Works**

- **Compares multiple conditions** using `<when>` and `<otherwise>`.
- **Executes the first matching condition** and ignores the rest.
- **Allows for a default case** using `<otherwise>`.
