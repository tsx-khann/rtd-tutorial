XML HttpRequest
===============
The XMLHttpRequest object is used to interact with servers in a web environment. It allows for the sending and receiving of data asynchronously.

Example of using XMLHttpRequest to fetch data:

.. code-block:: javascript

   var xhr = new XMLHttpRequest();
   xhr.open('GET', 'data.xml', true);
   xhr.onreadystatechange = function() {
       if (xhr.readyState == 4 && xhr.status == 200) {
           console.log(xhr.responseText);
       }
   }
   xhr.send();
