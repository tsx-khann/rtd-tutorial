XQuery_FLWOR
=============
FLWOR (For, Let, Where, Order by, Return) is the heart of XQuery, providing a structured way to filter and transform data.

Example:

  .. code-block:: xquery

      for $book in //book
      where $book/price < 20
      order by $book/title
      return $book/title
