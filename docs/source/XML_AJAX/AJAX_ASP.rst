AJAX ASP
========

AJAX allows web pages to communicate with an ASP (Active Server Pages) server **without reloading**. It is commonly used to fetch or update data dynamically.


**Example:** Fetch Data from an ASP Script.

**1. JavaScript (AJAX Request)**

.. code-block:: javascript

    function loadData() {
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          document.getElementById("demo").innerHTML = this.responseText;
        }
      };
      xhttp.open("GET", "server.asp", true);
      xhttp.send();
    }

**2. ASP Script (server.asp)**

.. code-block:: asp

    <% 
    Response.ContentType = "text/plain"
    Response.Write("Hello from ASP!")
    %>

When the page loads, `loadData()` sends an AJAX request to `server.asp`, which returns a response without refreshing the page.


**Why Use AJAX with ASP?**

- **Faster page updates without reloading**.
- **Retrieve or send data dynamically**.
- **Efficient server-side processing**.

