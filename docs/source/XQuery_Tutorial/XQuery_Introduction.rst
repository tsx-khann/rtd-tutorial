XQuery_Introduction
==========================

XQuery is a query and functional programming language designed to query and manipulate XML documents. It is similar to SQL for databases, but instead of databases, it works with XML documents.

Example:

    .. code-block:: xquery
  
        declare context item := document{"<book><title>XML Query</title></book>"};
        for $x in doc("books.xml")//book
        return $x/title
