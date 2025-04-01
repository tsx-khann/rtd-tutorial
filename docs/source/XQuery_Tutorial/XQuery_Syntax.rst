XQuery_Syntax
===============

The syntax of XQuery is similar to SQL, and it includes the following key components:

  -  Let: Assigns a variable.
  
  -  For: Iterates over a sequence.
  
  - Where: Filters data based on conditions.
  
  - Return: Specifies the output.

Example:

  .. code-block:: xquery
  
      let $book := <book><title>XML Query</title></book>
      return $book/title
