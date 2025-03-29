DTD Examples
============

Example of a complete DTD structure for an XML document.

.. code-block:: xml

   <!DOCTYPE note [
       <!ELEMENT note (to, from, heading, body)>
       <!ELEMENT to (#PCDATA)>
       <!ELEMENT from (#PCDATA)>
       <!ELEMENT heading (#PCDATA)>
       <!ELEMENT body (#PCDATA)>
   ]>
