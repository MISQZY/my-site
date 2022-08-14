function theme() {
  const toggleTheme = document.querySelector(".toggle-theme")
  let el = document.documentElement

  toggleTheme.addEventListener('click', () => {
    if (el.hasAttribute('data-theme')) {
      el.removeAttribute('data-theme')
      localStorage.removeItem('theme')
    } else {
      el.setAttribute('data-theme', 'light')
      localStorage.setItem('theme', 'light')
    }

  })

  if(localStorage.getItem('theme') !== null) {
    el.setAttribute('data-theme', 'light')
  }
}


theme()
