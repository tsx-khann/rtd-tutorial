AJAX XML File
=============

AJAX can fetch XML files and parse their contents dynamically.

**Example: Fetching and Displaying XML Data**

.. code-block:: javascript

    xhttp.open("GET", "data.xml", true);
    xhttp.send();

    xhttp.onload = function() {
      var xmlDoc = this.responseXML;
      var text = xmlDoc.getElementsByTagName("title")[0].childNodes[0].nodeValue;
      document.getElementById("demo").innerHTML = text;
    };
