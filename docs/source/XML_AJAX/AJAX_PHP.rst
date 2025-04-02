AJAX PHP
========

AJAX works with PHP to interact with databases and dynamically update webpage content.

**Example:** Fetching Data from a PHP Script.
**1. JavaScript AJAX Request**

.. code-block:: javascript

    xhttp.open("GET", "server.php", true);
    xhttp.send();

**2. PHP File (server.php)**

.. code-block:: php

    <?php
    echo "Hello, this is data from PHP!";
    ?>
