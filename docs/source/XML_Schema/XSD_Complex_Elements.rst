XSD Complex Elements
====================

Complex elements are elements that contain other elements or attributes. These elements can be defined using `<xs:complexType>`.

**Syntax:**

.. code-block:: xml

    <xs:complexType>
        <xs:sequence>
            <xs:element name="firstName" type="xs:string"/>
            <xs:element name="lastName" type="xs:string"/>
        </xs:sequence>
    </xs:complexType>

**Example:**

.. code-block:: xml

    <xs:element name="person">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="firstName" type="xs:string"/>
                <xs:element name="lastName" type="xs:string"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
