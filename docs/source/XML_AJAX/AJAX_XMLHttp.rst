AJAX XMLHttp
============

The `XMLHttpRequest` object is the core of AJAX. It allows JavaScript to make HTTP requests without reloading the page.

Basic syntax:
```javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "data.xml", true);
xhr.send();
