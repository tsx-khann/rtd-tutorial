DOM Create Nodes
========================
You can create new nodes using methods like createElement and createTextNode.

Example:

    .. code-block:: javascript
  
        var newBook = document.createElement("book");
        var newTitle = document.createElement("title");
        newTitle.textContent = "New Book Title";
        newBook.appendChild(newTitle);
        document.getElementById("books").appendChild(newBook);
