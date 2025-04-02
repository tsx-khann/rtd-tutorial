XSLT Examples
=============

Here are some **common use cases and examples** demonstrating how to apply XSLT for various transformations, including formatting, conditional logic, and sorting.

**Example 1: Sorting Elements**

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
        <book>
            <title>XML Fundamentals</title>
            <price>15</price>
        </book>
    </bookstore>

**2. XSLT Stylesheet for Sorting (transform.xsl)**

.. code-block:: xml

    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="/bookstore">
            <html>
                <body>
                    <h2>Books List Sorted by Price</h2>
                    <ul>
                        <xsl:for-each select="book">
                            <xsl:sort select="price" data-type="number" order="ascending"/>
                            <li>
                                <xsl:value-of select="title"/> - 
                                <xsl:value-of select="price"/>
                            </li>
                        </xsl:for-each>
                    </ul>
                </body>
            </html>
        </xsl:template>
    </xsl:stylesheet>

**Example 2: Conditional Logic**

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

**2. XSLT Stylesheet for Conditional Logic (transform.xsl)**

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
                                    <xsl:value-of select="title"/> (Premium Book)
                                </li>
                            </xsl:if>
                            <xsl:if test="price <= 30">
                                <li>
                                    <xsl:value-of select="title"/> (Regular Book)
                                </li>
                            </xsl:if>
                        </xsl:for-each>
                    </ul>
                </body>
            </html>
        </xsl:template>
    </xsl:stylesheet>
