XSD Example
===========

Here is a simple example of an XML Schema Definition (XSD) that defines a `person` element with `name` and `age` elements.

**Example XSD:**

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

**XML Document:**

.. code-block:: xml

    <person>
        <name>John Doe</name>
        <age>30</age>
    </person>
