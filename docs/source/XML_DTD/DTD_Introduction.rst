DTD Introduction
================

Document Type Definition (DTD) defines the structure and rules of an XML document.
It ensures that XML data is valid and follows a specific format.

Example:

.. code-block:: xml

   <!DOCTYPE note [
       <!ELEMENT note (to, from, heading, body)>
       <!ELEMENT to (#PCDATA)>
       <!ELEMENT from (#PCDATA)>
       <!ELEMENT heading (#PCDATA)>
       <!ELEMENT body (#PCDATA)>
   ]>
