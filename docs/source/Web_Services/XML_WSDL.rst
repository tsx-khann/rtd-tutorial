XML WSDL
=========

WSDL (Web Services Description Language) is an XML-based language used to describe the functionality offered by a web service. It provides a model for how the service can be accessed and what operations are available.

**Example WSDL:**

.. code-block:: xml

    <definitions xmlns="http://schemas.xmlsoap.org/wsdl/" 
                 xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
                 xmlns:http="http://schemas.xmlsoap.org/wsdl/http">
        <types>
            <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
                <xsd:element name="getPersonDetails" type="xsd:string"/>
            </xsd:schema>
        </types>
        <message name="GetPersonRequest">
            <part name="parameters" element="xsd:getPersonDetails"/>
        </message>
        <portType name="PersonServicePortType">
            <operation name="getPersonDetails">
                <input message="tns:GetPersonRequest"/>
            </operation>
        </portType>
        <binding name="PersonServiceBinding" type="tns:PersonServicePortType">
            <soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http"/>
            <operation name="getPersonDetails">
                <soap:operation soapAction="urn:getPersonDetails"/>
                <input>
                    <soap:body use="encoded" namespace="urn:PersonService" encodingStyle="http://schemas.xmlsoap.org/soap/encoding"/>
                </input>
            </operation>
        </binding>
        <service name="PersonService">
            <port name="PersonServicePort" binding="tns:PersonServiceBinding">
                <soap:address location="http://www.example.com/soap/personService"/>
            </port>
        </service>
    </definitions>
