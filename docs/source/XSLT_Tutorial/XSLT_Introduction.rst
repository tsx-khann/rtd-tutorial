XSLT Introduction
================

XSLT (Extensible Stylesheet Language Transformations) is used to **transform XML documents** into different formats like HTML, plain text, or other XML formats. It allows you to **apply templates** to XML data, transforming it into a desired format.


**Example:** Simple XSLT Transformation

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


**What Does XSLT Do?**

- **Transforms XML into various formats**, including HTML and text.
- **Uses templates** to match and manipulate XML data.
