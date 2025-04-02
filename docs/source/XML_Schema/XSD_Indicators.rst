XSD Indicators
==============

Indicators like `minOccurs` and `maxOccurs` are used to define the number of occurrences of an element in XSD.

**Example:**

.. code-block:: xml

    <xs:element name="phone" minOccurs="1" maxOccurs="3" type="xs:string"/>
