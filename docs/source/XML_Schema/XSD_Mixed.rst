XSD Mixed
=========

Mixed content elements can contain both text and other child elements. This is useful when the element needs to contain both plain text and child elements.

**Syntax:**

.. code-block:: xml

    <xs:complexType mixed="true">
        <xs:sequence>
            <xs:element name="firstName" type="xs:string"/>
            <xs:element name="lastName" type="xs:string"/>
        </xs:sequence>
    </xs:complexType>
