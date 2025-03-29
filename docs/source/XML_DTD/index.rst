XML DTD
=======

.. toctree::
   :maxdepth: 2

   DTD_Introduction
   DTD_Building_Blocks
   DTD_Elements
   DTD_Attributes
   DTD_Elements_vs_Attr
   DTD_Entities
   DTD_Examples


DTD Entities
============

Entities define reusable content that can be referenced multiple times in an XML document.

Example:

.. code-block:: xml

   <!ENTITY company "Tech Corp">
   <note>&company; welcomes you.</note>

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
