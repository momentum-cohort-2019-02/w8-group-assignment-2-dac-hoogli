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

// AJAX for posting
function questionDetail () {
  console.log('create question detail page is working!') // sanity check
}
    // .ajax({
    //   url: 'question_detail/', // the endpoint
    //   type: 'POST', // http method
    //   data: { the_question : ('#question-text').val() }, // data sent with the post request
      // handle a successful response
      // success: function(json) {
      //   ('#question-text').val(''); // remove the value from the input
      //   console.log(json); // log the returned json to the console
        // ('#talk').prepend('<li><strong>'+json.text+'</strong> - <em> '+json.author+'<em> - <span> '+json.created+'</span> - <a id='delete-post-'+json.postslug+''>delete me</a></li>');
        // console.log("success");
      // },
      // handle a non-successful response
//       error : function(xhr,errmsg,err) {
//           ('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//               " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//           console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//       }
//   });
// };