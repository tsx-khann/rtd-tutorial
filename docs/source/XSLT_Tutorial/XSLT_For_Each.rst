XSLT <for-each>
===============

The `<for-each>` element is used to **loop through XML nodes** and apply transformations to each one.



**Example:** Using `<for-each>`

**1. XML Document (input.xml)**

.. code-block:: xml

    <bookstore>
        <book>
            <title>Learn XSLT</title>
        </book>
        <book>
            <title>Mastering XML</title>
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



**How `<for-each>` Works**

- **Loops through a set of XML nodes**.
- **Applies transformations** to each node in the loop.
