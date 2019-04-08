


function answerFunction(){
  alert("thank you for your answer!");

}

function questionFunction(){
  alert("thank you for your question!");
}




var popup1 = document.getElementById("popup-1")
var openPopup1 = document.getElementById("open-popup-1")
var closePopup1 = document.getElementById('close-popup-1')

openPopup1.addEventListener('click', () => {
	popup1.style.display = "block";
})

closePopup1.addEventListener('click', () => {
	popup1.style.display = "none";
})

const Cookies = require('js-cookie')
const deepmerge = require('deepmerge')

function q (selector) {
  return document.querySelector(selector)
}

function request (url, options) {
if (!options) {
  options = {}
}

const defaultOptions = {
  headers: { 'X-CSRFToken': Cookies.get('csrftoken'), 'X-Requested-With': 'XMLHttpRequest' }
}
return fetch(url, deepmerge(defaultOptions, options))
}

function markAnswerStarred (answerHashid) {
request(`/answers/${answerHashid}/starred/`, { method: 'POST' })
  .then(response => {
    if (!response.ok) {
      throw Error(response.statusText)
    }
    return response.json()
  })
  .then(function (responseData) {
    if (responseData.complete) {
      let answer = q(`#answer-${responseData.id}`)
      answer.remove()
    }
  })
}
document.addEventListener('DOMContentLoaded', function () {
const answerList = q('#answer-list')
answerList.addEventListener('submit', function (event) {
  if (checkElementTypeAndClass(event.target, 'form', 'mark-answer-starred')) {
    event.preventDefault()
    const form = event.target
    markAnswerStarred(form.dataset['answerHashid'])
  }
})

