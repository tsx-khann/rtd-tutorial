XQuery_Example
==============
Here’s a basic example of an XQuery expression to select all titles from an XML document:

Example:

  .. code-block:: xquery
  
      declare context item := document{"<bookstore><book><title>Learning XQuery</title></book></bookstore>"};
      for $x in doc("books.xml")//book
      return $x/title
