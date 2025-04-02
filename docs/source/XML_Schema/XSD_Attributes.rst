XSD Attributes
==============

Attributes in XSD are defined using the `<xs:attribute>` element. Attributes are used to describe properties of elements.

**Syntax:**

.. code-block:: xml

    <xs:attribute name="id" type="xs:int"/>

**Example:**

.. code-block:: xml

    <xs:element name="person">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="name" type="xs:string"/>
                <xs:element name="age" type="xs:int"/>
            </xs:sequence>
        </xs:complexType>
        <xs:attribute name="id" type="xs:int"/>
    </xs:element>
