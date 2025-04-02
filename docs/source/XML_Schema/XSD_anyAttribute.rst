XSD <anyAttribute>
=================

The `<xs:anyAttribute>` element is used to allow attributes from other namespaces to be included in an XML document. This is helpful for extending the XML schema with attributes from external schemas.

**Syntax:**

.. code-block:: xml

    <xs:element name="person">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="firstName" type="xs:string"/>
                <xs:element name="lastName" type="xs:string"/>
            </xs:sequence>
            <xs:anyAttribute/>
        </xs:complexType>
    </xs:element>
