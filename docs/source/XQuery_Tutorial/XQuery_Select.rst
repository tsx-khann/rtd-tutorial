XQuery_Select
=============
You can use XQuery to select specific elements from an XML document.

Example:

  .. code-block:: xquery

      declare context item := document{"<store><book><title>Learning XQuery</title></book></store>"};
      for $x in //book
      return $x/title
