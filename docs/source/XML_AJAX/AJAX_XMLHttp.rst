AJAX XMLHttp
============

The `XMLHttpRequest` object enables JavaScript to send and receive data asynchronously without refreshing the webpage.

**Key Properties of XMLHttpRequest**

- readyState – Holds the status of the request (0-4).
- status – HTTP response code (e.g., 200 for success, 404 for not found).
- responseText – The response as a text string.
- responseXML – The response as an XML document.

**Example: Creating an XMLHttpRequest Object**

.. code-block:: javascript

    var xhttp = new XMLHttpRequest();
