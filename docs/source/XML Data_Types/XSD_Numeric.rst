XSD Numeric
===========

The `xs:numeric` types are used to define numeric values. Common subtypes include `xs:decimal`, `xs:integer`, `xs:float`, and `xs:double`.

**Example XSD (xs:decimal):**

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="price" type="xs:decimal"/>
    </xs:schema>

**XML Document:**

.. code-block:: xml

    <price>19.99</price>

**Example XSD (xs:integer):**

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="quantity" type="xs:integer"/>
    </xs:schema>

**XML Document:**

.. code-block:: xml

    <quantity>10</quantity>

**Example XSD (xs:float):**

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="temperature" type="xs:float"/>
    </xs:schema>

**XML Document:**

.. code-block:: xml

    <temperature>36.6</temperature>
