AJAX Examples
=============

This section contains practical AJAX examples.

**Example:** Fetching JSON Data with AJAX
**1. JavaScript (AJAX Request)**

.. code-block:: javascript

    xhttp.open("GET", "data.json", true);
    xhttp.onload = function() {
      var data = JSON.parse(this.responseText);
      document.getElementById("demo").innerHTML = data.name;
    };
    xhttp.send();

**2. JSON Data File (data.json)**

.. code-block:: json

    {
      "name": "John Doe",
      "age": 30,
      "city": "New York"
    }
