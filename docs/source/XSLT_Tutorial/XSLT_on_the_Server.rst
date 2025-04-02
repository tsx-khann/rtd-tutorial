XSLT on the Server
==================

The `<xsl:stylesheet>` element can also be applied **on the server-side**, where the XML transformation is done server-side before sending the transformed document to the client. This allows dynamic generation of HTML or other formats based on the XML content.

**Example:** Applying XSLT on the Server with PHP

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
                            <li>
                                <xsl:value-of select="title"/>
                            </li>
                        </xsl:for-each>
                    </ul>
                </body>
            </html>
        </xsl:template>
    </xsl:stylesheet>

**3. PHP Code for Applying XSLT (server-side)**

.. code-block:: php

    <?php
    $xml = new DOMDocument;
    $xml->load('input.xml');
    
    $xslt = new XSLTProcessor;
    $xsl = new DOMDocument;
    $xsl->load('transform.xsl');
    
    $xslt->importStylesheet($xsl);
    echo $xslt->transformToXML($xml);
    ?>
