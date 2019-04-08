window.addEventListener('DOMContentLoaded', (event) => {
  console.log('DOM fully loaded and parsed')

  const popup1 = document.getElementById('popup-1')
  const openPopup1 = document.getElementById('open-popup-1')
  const closePopup1 = document.getElementById('close-popup-1')

  openPopup1.addEventListener('click', () => {
    popup1.style.display = 'block'
  })
  closePopup1.addEventListener('click', () => {
    popup1.style.display = 'none'
  })
})

function answerFunction () {
  window.alert('thank you for your answer!')
}
function questionFunction () {
  window.alert('thank you for your question!')
}
