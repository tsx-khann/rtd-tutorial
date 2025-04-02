AJAX Request
============

AJAX requests use the `XMLHttpRequest` object to send data to a server.

**GET vs POST Requests**

- **GET** is used for retrieving data (faster, cached by browser).
- **POST** is used for sending data (more secure, no size limit).

**Example: Sending a GET Request**

.. code-block:: javascript

    xhttp.open("GET", "data.txt", true);
    xhttp.send();

**Example: Sending a POST Request**

.. code-block:: javascript

    xhttp.open("POST", "submit.php", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("name=John&age=30");
