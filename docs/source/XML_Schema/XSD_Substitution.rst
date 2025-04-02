XSD Substitution
================

Substitution groups allow an element to be substituted by another element in XSD. This can be useful when you want to create a family of elements that share the same name but are substituted dynamically.

**Syntax:**

.. code-block:: xml

    <xs:element name="person" substitutionGroup="employee"/>
    <xs:element name="employee" type="xs:string"/>
