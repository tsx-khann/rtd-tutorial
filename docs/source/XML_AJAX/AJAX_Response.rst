AJAX Response
=============

Once the server processes an AJAX request, it sends back a response.

**Handling AJAX Responses**

- **responseText** – Use for plain text or HTML responses.
- **responseXML** – Use for XML responses.

**Example: Handling a Text Response**

.. code-block:: javascript

    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("demo").innerHTML = this.responseText;
      }
    };
