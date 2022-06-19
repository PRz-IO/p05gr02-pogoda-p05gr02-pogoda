console.log("Hello world");

function przelaczanie() {
    var x = document.getElementById("tydzien");
    var y = document.getElementById("godzina")
    if (x.style.display === "none") {
      document.getElementById("prz2").textContent="Pogoda godzinowa";
      x.style.display = "block";
      y.style.display = "none";
    } else {
      document.getElementById("prz2").textContent="Pogoda dzienna";
      x.style.display = "none";
      y.style.display = "block";
    }
  }
  
function przelaczanie1() {
    var x = document.getElementById("tydzien1");
    var y = document.getElementById("godzina1")
    if (x.style.display === "none") {
      document.getElementById("prz1").textContent="Pogoda godzinowa";
      x.style.display = "block";
      y.style.display = "none";
    } else {
      document.getElementById("prz1").textContent="Pogoda dzienna";
      x.style.display = "none";
      y.style.display = "block";
    }
  }

function wyszukiwarka() {
    var x = document.getElementById("miastaUzytkownika");
    var y = document.getElementById("wyszukiwarka")
    if (x.style.display === "none") {
      document.getElementById("wysz").textContent="Wyszukiwarka";
      x.style.display = "block";
      y.style.display = "none";
    } else {
      document.getElementById("wysz").textContent="Twoje miasta";
      x.style.display = "none";
      y.style.display = "block";
    }
  }