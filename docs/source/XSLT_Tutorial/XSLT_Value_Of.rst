XSLT <value-of>
===============

The `<value-of>` element is used to **extract values** from XML and insert them into the transformed output.



**Example:** Using `<value-of>`

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
                        <li>
                            <xsl:value-of select="book/title"/>
                        </li>
                    </ul>
                </body>
            </html>
        </xsl:template>
    </xsl:stylesheet>



**How `<value-of>` Works**

- **Extracts data** from the XML source.
- **Inserts values** into the output document.
