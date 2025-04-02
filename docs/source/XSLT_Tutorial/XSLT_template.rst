XSLT <template>
============

The `<template>` element in XSLT defines a **template rule**. It matches specific nodes in the source XML document and applies a transformation to them.

**Example:** Using `<template>`

**1. XML Document (input.xml)**

.. code-block:: xml

    <bookstore>
        <book>
            <title>Learn XSLT</title>
            <price>35</price>
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

- **Defines transformation rules** for matching nodes.
- **Allows for reusable templates** that process specific parts of the XML document.

---

XSLT <value-of>
==============

The `<value-of>` element in XSLT is used to **extract** the value of a selected node and output it as text.

**Example:** Using `<value-of>`

**1. XML Document (input.xml)**

.. code-block:: xml

    <bookstore>
        <book>
            <title>Learn XSLT</title>
            <price>35</price>
