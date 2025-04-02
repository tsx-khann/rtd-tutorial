XSLT Edit XML
==============

XSLT allows **editing XML content** before transforming it, such as modifying values, adding new elements, or changing the structure. This is useful when you need to dynamically modify XML content during transformation.

**Example:** Editing XML with XSLT

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

**2. XSLT Stylesheet for Editing (transform.xsl)**

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
                                    <xsl:value-of select="title"/> - 
                                    <xsl:value-of select="price"/>
                                </li>
                            </xsl:if>
                            <xsl:if test="price <= 30">
                                <li>
                                    <xsl:value-of select="title"/> (Discounted Price) - 
                                    <xsl:value-of select="price"/>
                                </li>
                            </xsl:if>
                        </xsl:for-each>
                    </ul>
                </body>
            </html>
        </xsl:template>
    </xsl:stylesheet>
