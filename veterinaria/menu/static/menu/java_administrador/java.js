
let slideIndex = 1;

function plusSlides(n) {
  showSlides(slideIndex += n);
}
function currentSlide(n) {
  showSlides(slideIndex = n);
}
function showSlides(currentSlide) {
  let slides = document.getElementsByClassName("carousel__item");
  if (currentSlide > slides.length) { slideIndex = 1 }
  if (currentSlide < 1) {slideIndex= slides.length }
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex - 1].style.display = "block";

}
showSlides(slideIndex);