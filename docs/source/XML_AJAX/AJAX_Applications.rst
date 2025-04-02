AJAX Applications
=================

AJAX is used in various real-world applications, including:

- **Live search** (Google Suggest, real-time filtering).
- **Chat applications** (real-time messaging).
- **Auto-refreshing news feeds**.

**Example:** Auto-Refreshing Content with AJAX.

.. code-block:: javascript

    setInterval(function() {
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          document.getElementById("liveData").innerHTML = this.responseText;
        }
      };
      xhttp.open("GET", "fetch_data.php", true);
      xhttp.send();
    }, 5000); // Refresh every 5 seconds
