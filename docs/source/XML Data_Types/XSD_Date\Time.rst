XSD Date/Time
=============

The `xs:date` and `xs:dateTime` data types are used to represent date and time values. `xs:date` only includes a date, while `xs:dateTime` includes both a date and time.

**Example XSD:**

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="event">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="eventDate" type="xs:date"/>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
    </xs:schema>

**XML Document:**

.. code-block:: xml

    <event>
        <eventDate>2025-04-02</eventDate>
    </event>

**Example XSD with Date and Time:**

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="meeting">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="startDateTime" type="xs:dateTime"/>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
    </xs:schema>

**XML Document:**

.. code-block:: xml

    <meeting>
        <startDateTime>2025-04-02T10:00:00</startDateTime>
    </meeting>
