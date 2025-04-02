XML RDF
========

RDF (Resource Description Framework) is a framework used for representing metadata and relationships between data on the web. It allows data to be linked in a way that can be understood by machines.

**Example RDF:**

.. code-block:: xml

    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
             xmlns:ex="http://www.example.org/">
        <rdf:Description rdf:about="http://www.example.org/person/12345">
            <ex:name>John Doe</ex:name>
            <ex:age>30</ex:age>
        </rdf:Description>
    </rdf:RDF>
