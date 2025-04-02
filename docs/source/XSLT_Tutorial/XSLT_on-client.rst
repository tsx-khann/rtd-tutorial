XSLT on the Client
=================

XSLT can be applied directly on the **client-side** using JavaScript and the browser's built-in XSLT processor.

**Example:** Using XSLT on the Client

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

**How to Apply XSLT on the Client**

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <title>XSLT on Client</title>
    </head>
    <body>
        <div id="result"></div>
    
        <script type="text/javascript">
            var xml = loadXMLDoc("input.xml");
            var xsl = loadXMLDoc("transform.xsl");
    
            // Apply XSLT transformation
            var xsltProcessor = new XSLTProcessor();
            xsltProcessor.importStylesheet(xsl);
            var resultDocument = xsltProcessor.transformToFragment(xml, document);
            document.getElementById("result").appendChild(resultDocument);
    
            function loadXMLDoc(filename) {
                var xhttp = new XMLHttpRequest();
                xhttp.open("GET", filename, false);
                xhttp.send();
                return xhttp.responseXML;
            }
        </script>
    </body>
    </html>
