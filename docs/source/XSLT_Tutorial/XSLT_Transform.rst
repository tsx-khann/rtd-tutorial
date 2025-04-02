XSLT Transform
==============

XSLT uses templates to **transform XML documents** into different formats. This transformation is done by applying an XSLT stylesheet to an XML document.



**Example:** Basic XSLT Transformation

**1. XML Document (input.xml)**

.. code-block:: xml

    <bookstore>
        <book>
            <title>Learn XSLT</title>
            <author>John Doe</author>
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
                            <li>
                                <xsl:value-of select="title"/>
                            </li>
                        </xsl:for-each>
                    </ul>
                </body>
            </html>
        </xsl:template>
    </xsl:stylesheet>


**How XSLT Works**

- **Applies templates** to XML data.
- **Transforms XML into HTML, text**, or other formats.
