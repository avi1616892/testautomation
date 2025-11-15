console.log("Welcome to Rosie Huntington-Whiteley page!");

// שינוי רקע בלחיצה על כפתור
function changeBackground() {
    const colors = ["#bfeeff", "#ffe4e1", "#e6ffe6", "#fffacd"];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    document.body.style.backgroundColor = randomColor;
}
