XML SOAP
=========

SOAP (Simple Object Access Protocol) is a protocol for exchanging structured information in the implementation of web services. It uses XML to encode the message and relies on other application layer protocols, such as HTTP or SMTP, for message negotiation and transmission.

**Example SOAP Request:**

.. code-block:: xml

    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                      xmlns:web="http://www.example.com/webservice">
        <soapenv:Header/>
        <soapenv:Body>
            <web:getPersonDetails>
                <web:personId>12345</web:personId>
            </web:getPersonDetails>
        </soapenv:Body>
    </soapenv:Envelope>
