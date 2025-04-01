XML XSLT
========

XSLT (Extensible Stylesheet Language Transformations) is used to transform XML data into different formats like HTML, text, or other XML formats.

Example of transforming XML with XSLT:

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
       <xsl:template match="/">
           <html>
               <body>
                   <h1>Books</h1>
                   <table border="1">
                       <tr>
                           <th>Title</th>
                           <th>Author</th>
                       </tr>
                       <xsl:for-each select="catalog/book">
                           <tr>
                               <td><xsl:value-of select="title"/></td>
                               <td><xsl:value-of select="author"/></td>
                           </tr>
                       </xsl:for-each>
                   </table>
               </body>
           </html>
       </xsl:template>
   </xsl:stylesheet>
