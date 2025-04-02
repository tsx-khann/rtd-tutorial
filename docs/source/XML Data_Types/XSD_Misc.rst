XSD Misc
========

The `xs:misc` category includes other data types like `xs:boolean`, `xs:base64Binary`, `xs:hexBinary`, etc., that don't fit neatly into string, numeric, or date/time categories.

**Example XSD (xs:boolean):**

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="isAvailable" type="xs:boolean"/>
    </xs:schema>

**XML Document:**

.. code-block:: xml

    <isAvailable>true</isAvailable>
