DTD Building Blocks
===================

DTDs consist of elements, attributes, entities, and notations.
They define the valid structure of an XML document.

Example:

.. code-block:: xml

   <!ELEMENT note (to, from, heading, body)>
   <!ATTLIST note date CDATA #REQUIRED>
