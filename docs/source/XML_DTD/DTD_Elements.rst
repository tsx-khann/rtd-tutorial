DTD Elements
============

Elements define the structure and content of an XML document.
They specify what child elements or text data they can contain.

Example:

.. code-block:: xml

   <!ELEMENT note (to, from, heading, body)>
   <!ELEMENT to (#PCDATA)>
