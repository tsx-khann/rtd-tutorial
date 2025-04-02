XSD <any>
=========

The `<xs:any>` element allows you to include elements from other namespaces in your XML schema. This is useful for defining a more flexible schema.

**Syntax:**

.. code-block:: xml

    <xs:element name="anyElement">
        <xs:complexType>
            <xs:sequence>
                <xs:any minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
