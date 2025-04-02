XSD Reference
=============

The `xs:reference` data type is used to reference other elements defined in the schema. This is helpful for reusing complex types or groups of elements.

**Example XSD:**

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="name" type="xs:string"/>
        <xs:element name="address" type="xs:string"/>
        <xs:element name="person">
            <xs:complexType>
                <xs:sequence>
                    <xs:element ref="name"/>
                    <xs:element ref="address"/>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
    </xs:schema>

**XML Document:**

.. code-block:: xml

    <person>
        <name>John Doe</name>
        <address>123 Elm Street</address>
    </person>
