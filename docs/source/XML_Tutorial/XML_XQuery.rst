XML XQuery
===========
XQuery is a language designed to query and manipulate XML data. It allows for complex searches and transformations of XML documents.

Example:

.. code-block:: xquery

   for $book in //book
   return <book>{ $book/title }</book>
