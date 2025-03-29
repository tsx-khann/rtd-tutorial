XML DTD
=======

.. toctree::
   :maxdepth: 2

   DTD Introduction
   DTD Building Blocks
   DTD Elements
   DTD Attributes
   DTD Elements vs Attr
   DTD Entities
   DTD Examples





DTD Elements
============

Elements define the structure and content of an XML document.
They specify what child elements or text data they can contain.

Example:

.. code-block:: xml

   <!ELEMENT note (to, from, heading, body)>
   <!ELEMENT to (#PCDATA)>

DTD Attributes
==============

Attributes provide additional information about elements.
They are defined in the DTD using `ATTLIST`.

Example:

.. code-block:: xml

   <!ATTLIST note date CDATA #REQUIRED>

DTD Elements vs Attr
====================

Elements define data structure, while attributes provide metadata.
Using elements or attributes depends on the design choice.

Example:

Elements:

.. code-block:: xml

   <note>
       <date>2024-06-01</date>
   </note>

Attributes:

.. code-block:: xml

   <note date="2024-06-01">
   </note>

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
