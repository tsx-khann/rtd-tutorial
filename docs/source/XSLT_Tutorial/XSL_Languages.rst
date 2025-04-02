XSL Languages
=============

XSL (Extensible Stylesheet Language) is a language for defining the presentation of XML data. It consists of three parts:

- **XSLT**: For transforming XML.
- **XPath**: For navigating XML.
- **XSL-FO**: For formatting XML content for printing.



**Example:** Using XPath with XSLT

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


**Key Parts of XSL**

- **XSLT**: Transforms XML into different formats.
- **XPath**: Queries and navigates XML content.
- **XSL-FO**: Formatting objects for printed output.
