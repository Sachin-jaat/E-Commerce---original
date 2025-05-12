const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');
let index = 0;

function showSlide(i) {
  slides.forEach((slide, idx) => {
    slide.classList.toggle('active', idx === i);
    dots[idx].classList.toggle('active', idx === i);
  });
  index = i;
}

function nextSlide() {
  index = (index + 1) % slides.length;
  showSlide(index);
}

// Link dots to slides
dots.forEach(dot => {
  dot.addEventListener('click', () => {
    const dotIndex = parseInt(dot.getAttribute('data-index'));
    showSlide(dotIndex);
  });
});

setInterval(nextSlide, 2000); 



  const slides2 = document.querySelectorAll('.slide2');
  const dots2 = document.querySelectorAll('.dot2');
  let currentIndex2 = 0;

  function showSlide2(index) {
    slides2.forEach((slide, i) => {
      slide.classList.toggle('active2', i === index);
      dots2[i].classList.toggle('active', i === index);
    });
    currentIndex2 = index;
  }

  dots2.forEach(dot => {
    dot.addEventListener('click', () => {
      const idx = parseInt(dot.getAttribute('data-index'));
      showSlide2(idx);
    });
  });

  
  setInterval(() => {
    const nextIndex = (currentIndex2 + 1) % slides2.length;
    showSlide2(nextIndex);
  }, 5000);



  const slides3 = document.querySelectorAll('.slide3');
  const dots3 = document.querySelectorAll('.dot3');
  let currentIndex3 = 0;

  function showSlide3(index) {
    slides3.forEach((slide, i) => {
      slide.classList.toggle('active3', i === index);
      dots3[i].classList.toggle('active', i === index);
    });
    currentIndex3 = index;
  }

  dots3.forEach(dot => {
    dot.addEventListener('click', () => {
      const idx = parseInt(dot.getAttribute('data-index'));
      showSlide3(idx);
    });
  });

  setInterval(() => {
    const nextIndex = (currentIndex3 + 1) % slides3.length;
    showSlide3(nextIndex);
  }, 3000);


 
  const slides4 = document.querySelectorAll('.slide4');
  const dots4 = document.querySelectorAll('.dot4');
  let currentIndex4 = 0;

  function showSlide4(index) {
    slides4.forEach((slide, i) => {
      slide.classList.toggle('active4', i === index);
      dots4[i].classList.toggle('active', i === index);
    });
    currentIndex4 = index;
  }

  dots4.forEach(dot => {
    dot.addEventListener('click', () => {
      const idx = parseInt(dot.getAttribute('data-index'));
      showSlide4(idx);
    });
  });

  setInterval(() => {
    const nextIndex = (currentIndex4 + 1) % slides4.length;
    showSlide4(nextIndex);
  }, 3000);



 
  const slides5 = document.querySelectorAll('.slide5');
  const dots5 = document.querySelectorAll('.dot5');
  let currentIndex5 = 0;

  function showSlide5(index) {
    slides5.forEach((slide, i) => {
      slide.classList.toggle('active5', i === index);
      dots5[i].classList.toggle('active', i === index);
    });
    currentIndex5 = index;
  }

  dots5.forEach(dot => {
    dot.addEventListener('click', () => {
      const idx = parseInt(dot.getAttribute('data-index'));
      showSlide5(idx);
    });
  });

  setInterval(() => {
    const nextIndex = (currentIndex5 + 1) % slides5.length;
    showSlide5(nextIndex);
  }, 4000);


  function showPage(pageNumber) {
    const pages = document.querySelectorAll('.page');
    pages.forEach((page, index) => {
      page.style.display = (index + 1 === pageNumber) ? 'grid' : 'none';
    });
  }


  document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const success = true; 

    if (success) {
       
        window.location.href = 'homepage.html'; 
    } else {
        alert('Signup failed. Please try again.');
    }
});


  function showPage(pageNum) {
    document.querySelectorAll('.product-grid.page').forEach(p => p.style.display = 'none');
    document.getElementById(`page${pageNum}`).style.display = 'grid';
  }
