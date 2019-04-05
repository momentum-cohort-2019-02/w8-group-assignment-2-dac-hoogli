window.addEventListener('DOMContentLoaded', (event) => {
  console.log('DOM fully loaded and parsed')
  document.querySelector('#questionForm').addEventListener('submit', function (event) {
    event.preventDefault()
    const questionTitle = document.querySelector('#id_title')
    const questionAuthor = document.querySelector('#id_author')
    const questionDescription = document.querySelector('#id_description')
    console.log('form submitted!', event.target, questionTitle.value, questionAuthor.value, questionDescription.value)
    questionDetail()
  })
})

// AJAX for posting questions
function questionDetail () {
  console.log('create question detail page is working!') // sanity check
}
