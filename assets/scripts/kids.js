// Крихітні конфеті при кліку по головному заголовку
(function () {
  const h1 = document.querySelector('.hero h1');
  if (!h1) return;
  h1.style.cursor = 'pointer';
  h1.addEventListener('click', () => {
    const el = document.createElement('div');
    el.textContent = '🎉';
    el.style.position = 'fixed';
    el.style.left = (Math.random() * 80 + 10) + 'vw';
    el.style.top = '-20px';
    el.style.fontSize = (Math.random() * 20 + 18) + 'px';
    el.style.transition = 'transform 1.2s ease, opacity 1.2s ease';
    document.body.appendChild(el);
    requestAnimationFrame(() => {
      el.style.transform = 'translateY(110vh) rotate(' + (Math.random()*360) + 'deg)';
      el.style.opacity = 0;
    });
    setTimeout(() => el.remove(), 1300);
  });
})();
