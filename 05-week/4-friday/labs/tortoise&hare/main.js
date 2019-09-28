function animateIt(elementId, speed) {
    var elem = document.getElementById(elementId);
  
    tick = 0;
  
    var timer = setInterval(function() { 
      if (tick < 500) {
        elem.style.left = tick * speed + "px";  
        tick++;
      }
      else {clearInterval(timer);}
      }, 30);
  }
  document.getElementById("start").addEventListener("click", animateIt('turtle', 1.5),animateIt('rabbit', 2.0));
  