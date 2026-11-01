(() => {
  const stages = [...document.querySelectorAll('.movement')];
  const links = [...document.querySelectorAll('.stage-nav a')];
  const bar = document.querySelector('.reading-progress');
  let pending = false;
  function update() {
    const max = document.documentElement.scrollHeight - innerHeight;
    bar.style.width = `${max > 0 ? Math.min(100, Math.max(0, scrollY / max * 100)) : 100}%`;
    let active = 0;
    stages.forEach((section, index) => { if (section.getBoundingClientRect().top <= innerHeight * .4) active = index; });
    links.forEach((link, index) => { if (index === active) link.setAttribute('aria-current', 'true'); else link.removeAttribute('aria-current'); });
    pending = false;
  }
  function schedule() { if (!pending) { pending = true; requestAnimationFrame(update); } }
  addEventListener('scroll', schedule, { passive: true });
  addEventListener('resize', schedule);
  addEventListener('load', update);
  update();
})();
