function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  function filterFunction() {
    var input, sizeFilter, colorFilter, dropdown, options, a, i, txtValue, size, color;
    input = document.getElementById("myInput");
    sizeFilter = document.getElementById("sizeFilter").value;
    colorFilter = document.getElementById("colorFilter").value;
    dropdown = document.getElementById("myDropdown");
    options = dropdown.getElementsByTagName("a");
    
    for (i = 0; i < options.length; i++) {
        a = options[i];
        txtValue = a.textContent || a.innerText;
        size = a.getAttribute("data-size");
        color = a.getAttribute("data-color");

        // Check if the text, size, and color match the filters
        if (
            txtValue.toUpperCase().indexOf(input.value.toUpperCase()) > -1 &&
            (sizeFilter === "all" || size === sizeFilter) &&
            (colorFilter === "all" || color === colorFilter)
        ) {
            options[i].style.display = "";
        } else {
            options[i].style.display = "none";
        }
    }


}