XQuery_HTML
============
XQuery can also be used to generate HTML content dynamically. Here’s an example of how to generate an HTML table using XQuery:

Example:

  .. code-block:: xquery
  
      declare context item := document{"<books><book><title>XML Query</title><author>John</author></book></books>"};
      <html>
          <table border="1">
              <tr><th>Title</th><th>Author</th></tr>
              { for $x in //book
                return <tr><td>{ $x/title }</td><td>{ $x/author }</td></tr> }
          </table>
      </html>
