import './main.scss'

function colorRatings(item, total_rating) {
  // Update stars coloring in form
  let selected_rating = item.charAt(item.length - 1);
  for (let i = 0; i < total_rating; i++) {
    if (i <= Number(selected_rating)) {
      document.getElementById('id_review-rating_' + i).classList.add('star-full')
      document.getElementById('id_review-rating_' + i).classList.remove('star-empty')
    } else {
      document.getElementById('id_review-rating_' + i).classList.add('star-empty')
      document.getElementById('id_review-rating_' + i).classList.remove('star-full')
    }
  }
}

document.addEventListener('DOMContentLoaded', function () {
  // Wait for document to be loaded
  let rating_inputs = document.querySelectorAll(
    '#rating input[name="review-rating"]');
  if (rating_inputs) {
    for (let item = 0; item < rating_inputs.length; item++) {
      // Event listener for checked item
      rating_inputs[item].addEventListener('click', function () {
        if (rating_inputs[item].checked) {
          colorRatings(rating_inputs[item].id, rating_inputs.length);
        }
      })
      // Set initial stars
      if (rating_inputs[item].checked) {
        colorRatings(rating_inputs[item].id, rating_inputs.length);
      }
    }
  }
}, false);