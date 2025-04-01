XML DTD
========
A Document Type Definition (DTD) defines the structure and rules for XML documents. It specifies what elements and attributes are allowed, and how they can be nested.

Example of DTD:

.. code-block:: dtd

   <!ELEMENT book (title, author)>
   <!ELEMENT title (#PCDATA)>
   <!ELEMENT author (#PCDATA)>
