XSD <schema>
===========

The `<xs:schema>` element is used to define an XML Schema, containing all the rules, data types, and structure for the XML document. It is the root element in an XSD file.

**Syntax:**

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <!-- Schema content here -->
    </xs:schema>

**Attributes of `<xs:schema>`:**

- `xmlns:xs`: Defines the XML Schema namespace.
- `targetNamespace`: Specifies the namespace for the XML Schema.
- `elementFormDefault`: Specifies whether elements should be qualified with a namespace.
