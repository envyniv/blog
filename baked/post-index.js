
function testFunction() { document.getElementById('testDropdown').classList.toggle('show'); }
function tilFunction() { document.getElementById('tilDropdown').classList.toggle('show'); }
function blogFunction() { document.getElementById('blogDropdown').classList.toggle('show'); }
    window.onclick = function(event) {
      if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }