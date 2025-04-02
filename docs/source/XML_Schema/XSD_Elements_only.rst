XSD Elements-only
=================

Elements-only types are complex types that contain only child elements and no attributes. These are defined using `<xs:sequence>` without attributes.

**Syntax:**

.. code-block:: xml

    <xs:complexType>
        <xs:sequence>
            <xs:element name="firstName" type="xs:string"/>
            <xs:element name="lastName" type="xs:string"/>
        </xs:sequence>
    </xs:complexType>
