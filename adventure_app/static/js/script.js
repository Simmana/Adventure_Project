
function triggerFileInput() {
    document.getElementById('fileInput').click();
}

// Функция для предварительного просмотра загруженного фото
function previewImage() {
    const fileInput = document.getElementById('fileInput');
    const profileImage = document.getElementById('profileImage');
    const defaultIcon = document.getElementById('defaultIcon');

    // Проверяем, загружен ли файл
    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();

        // Чтение файла и отображение в контейнере
        reader.onload = function(e) {
            profileImage.src = e.target.result;
            profileImage.style.display = 'block'; // Показываем изображение
            defaultIcon.style.display = 'none';  // Скрываем иконку пользователя
        };

        reader.readAsDataURL(fileInput.files[0]); // Чтение файла как URL
    }
}

function toggleGlow(button) {
    button.classList.toggle("glowing");
}
function MenuFilter() {
    let FilterMenu = document.getElementById("Filters");
    if (FilterMenu.style.display === "none") {
        FilterMenu.style.display = "block";
    } else {
        FilterMenu.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", function() {
  const leavesContainer = document.getElementById("leaves-container");
  
  if (!leavesContainer) {
      console.error('Элемент с id "leaves-container" не найден!');
      return;
  }

  function createLeaf() {
      const leaf = document.createElement("div");
      leaf.classList.add("leaf");
      leaf.style.left = Math.random() * 100 + "vw"; // Случайное положение по ширине
      leaf.style.top = "190px"; // Стартовое положение над экраном
      leavesContainer.appendChild(leaf);

      // Анимация падения листочков
      anime({
          targets: leaf,
          translateY: [0, window.innerHeight + 30], // Падает за пределы экрана
          translateX: {
              value: () => Math.random() * 50 - 25, // Легкое покачивание влево-вправо
              duration: 2000,
              easing: "easeInOutSine"
          },
          rotate: {
              value: () => Math.random() * 360,
              duration: 3000,
              easing: "easeInOutSine"
          },
          duration: 5000 + Math.random() * 3000, // Разная длительность падения
          easing: "linear",
          opacity: [1, 0], // Плавное исчезновение
          complete: function () {
              leaf.remove(); // Удаляем листочек после анимации
          }
      });
  }

  // Создаем листочки каждые 500 мс
  setInterval(createLeaf, 500);
});


  document.addEventListener("DOMContentLoaded", function() {
    fetchWeatherData();
});


document.addEventListener("DOMContentLoaded", function() {
  fetchWeatherData();
});

