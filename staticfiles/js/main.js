
const navbarlinksActive = () => {
  var miNav = document.querySelectorAll(".nav-link");
  // var miNavLinks = miNav.getElementsByTagName("a");
  for (var i = 0; i < miNav.length; i++) {
    miNav[i].onclick = function () {
      console.info(this.innerHTML);
    }
  };
  miNav.forEach(el => {
    el.onclick = function () {
      console.info(el.parentElement);
      el.parentElement.classList.add('bg-warning')
    }
  })
}

