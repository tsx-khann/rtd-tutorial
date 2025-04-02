XSD How To
==========

To create an XSD schema, follow these steps:

1. Declare the XML Schema using the `<xs:schema>` element.
2. Define the structure of your XML document using elements like `<xs:element>`, `<xs:complexType>`, and `<xs:simpleType>`.
3. Specify data types such as `xs:string`, `xs:int`, `xs:date`, etc.
4. Add constraints using attributes like `minOccurs`, `maxOccurs`, and `pattern`.

**Example:**

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="person">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="name" type="xs:string"/>
                    <xs:element name="age" type="xs:int"/>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
    </xs:schema>
