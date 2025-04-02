XSD Elements
============

Elements in XSD are defined using the `<xs:element>` tag. Elements represent the components of the XML document.

**Syntax:**

.. code-block:: xml

    <xs:element name="person" type="xs:string"/>

**Attributes of `<xs:element>`:**

- `name`: The name of the element.
- `type`: The data type of the element, such as `xs:string`, `xs:int`, etc.
- `minOccurs`: Minimum number of occurrences of the element.
- `maxOccurs`: Maximum number of occurrences of the element.

**Example:**

.. code-block:: xml

    <xs:element name="person">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="name" type="xs:string"/>
                <xs:element name="age" type="xs:int"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
