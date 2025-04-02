XSLT <template>
=================

The `<template>` element in XSLT defines **how to transform specific XML elements**. It matches elements in the XML document and applies a transformation rule.



**Example:** XSLT Template

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



**How `<template>` Works**
- **Defines rules for transforming elements**.
- **Matches XML data** and applies transformations.
