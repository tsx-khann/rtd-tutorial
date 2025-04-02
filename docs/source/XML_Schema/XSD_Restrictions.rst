XSD Restrictions
================

XSD allows you to define restrictions on elements and attributes, such as length, pattern, or range of values.

**Syntax:**

.. code-block:: xml

    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:minLength value="5"/>
        </xs:restriction>
    </xs:simpleType>

**Example:**

.. code-block:: xml

    <xs:element name="phone">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:pattern value="\d{3}-\d{3}-\d{4}"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:element>
