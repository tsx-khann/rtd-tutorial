XSD Empty
=========

An empty element is one that has no child elements or attributes. In XSD, an empty element can be defined with `<xs:empty>` or by using a complex type with no sequence or attributes.

**Syntax:**

.. code-block:: xml

    <xs:element name="note">
        <xs:complexType>
            <xs:sequence/>
        </xs:complexType>
    </xs:element>
