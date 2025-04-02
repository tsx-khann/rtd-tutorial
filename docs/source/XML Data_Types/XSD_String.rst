XSD String
===========

The `xs:string` data type is used to represent a sequence of characters in XML. This is often used for textual data such as names, addresses, and descriptions.

**Example XSD:**

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="person">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="name" type="xs:string"/>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
    </xs:schema>

**XML Document:**

.. code-block:: xml

    <person>
        <name>John Doe</name>
    </person>
