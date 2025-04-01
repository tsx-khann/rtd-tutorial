XML Schema
==========
An XML Schema is a more powerful alternative to DTD. It defines the structure and data types of an XML document, providing more flexibility and precision.

Example of XML Schema:

.. code-block:: xml

   <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
       <xs:element name="book">
           <xs:complexType>
               <xs:sequence>
                   <xs:element name="title" type="xs:string"/>
                   <xs:element name="author" type="xs:string"/>
               </xs:sequence>
           </xs:complexType>
       </xs:element>
   </xs:schema>
