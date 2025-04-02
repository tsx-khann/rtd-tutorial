AJAX Database
=============

AJAX enables real-time database communication.

**Example:** Live Search with AJAX and Database.

**1. JavaScript (Live Search Function)**

.. code-block:: javascript

    function showResult(str) {
      if (str.length == 0) {
        document.getElementById("livesearch").innerHTML = "";
        return;
      }
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          document.getElementById("livesearch").innerHTML = this.responseText;
        }
      };
      xhttp.open("GET", "search.php?q=" + str, true);
      xhttp.send();
    }

**2. PHP (Database Search Script - search.php)**

.. code-block:: php

    <?php
    $q = $_GET["q"];
    $con = mysqli_connect('localhost','root','','myDB');
    if (!$con) {
      die('Could not connect: ' . mysqli_error($con));
    }
    $sql="SELECT * FROM users WHERE name LIKE '%".$q."%'";
    $result = mysqli_query($con,$sql);
    while($row = mysqli_fetch_array($result)) {
      echo $row['name'] . "<br>";
    }
    mysqli_close($con);
    ?>
