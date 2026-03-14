// CUSTOM CURSOR
const cursor = document.getElementById('cursor');
const ring = document.getElementById('cursor-ring');
let mx = 0, my = 0, rx = 0, ry = 0;
document.addEventListener('mousemove', e => { mx = e.clientX; my = e.clientY; });
(function animCursor() {
  cursor.style.left = mx + 'px'; cursor.style.top = my + 'px';
  rx += (mx - rx) * 0.12; ry += (my - ry) * 0.12;
  ring.style.left = rx + 'px'; ring.style.top = ry + 'px';
  requestAnimationFrame(animCursor);
})();
document.querySelectorAll('a,button,.proj-card').forEach(el => {
  el.addEventListener('mouseenter', () => { cursor.style.width='20px'; cursor.style.height='20px'; cursor.style.background='var(--pink)'; cursor.style.boxShadow='0 0 30px var(--pink)'; });
  el.addEventListener('mouseleave', () => { cursor.style.width='12px'; cursor.style.height='12px'; cursor.style.background='var(--cyan)'; cursor.style.boxShadow='0 0 20px var(--cyan), 0 0 40px var(--cyan)'; });
});

// PARTICLE CANVAS
const canvas = document.getElementById('bg-canvas');
const ctx = canvas.getContext('2d');
function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
resize(); window.addEventListener('resize', resize);
const particles = Array.from({length:90}, () => ({
  x: Math.random()*canvas.width, y: Math.random()*canvas.height,
  r: Math.random()*1.5+0.3,
  vx: (Math.random()-0.5)*0.25, vy: (Math.random()-0.5)*0.25,
  color: ['#d4a373','#a47d52','#faedcd','#eaddcf'][Math.floor(Math.random()*4)],
  alpha: Math.random()*0.4+0.1
}));
(function drawParticles() {
  ctx.clearRect(0,0,canvas.width,canvas.height);
  for (let i=0; i<particles.length; i++) {
    const p = particles[i];
    p.x += p.vx; p.y += p.vy;
    if (p.x<0) p.x=canvas.width; if (p.x>canvas.width) p.x=0;
    if (p.y<0) p.y=canvas.height; if (p.y>canvas.height) p.y=0;
    ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
    ctx.fillStyle=p.color; ctx.globalAlpha=p.alpha; ctx.fill();
    for (let j=i+1; j<particles.length; j++) {
      const q=particles[j]; const dx=p.x-q.x, dy=p.y-q.y; const d=Math.sqrt(dx*dx+dy*dy);
      if (d<130) { ctx.beginPath(); ctx.moveTo(p.x,p.y); ctx.lineTo(q.x,q.y); ctx.strokeStyle=p.color; ctx.globalAlpha=(1-d/130)*0.07; ctx.lineWidth=0.5; ctx.stroke(); }
    }
  }
  ctx.globalAlpha=1; requestAnimationFrame(drawParticles);
})();

// SCROLL REVEAL
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('visible'); });
}, {threshold:0.1});
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// HERO MOUSE GLOW
document.getElementById('hero').addEventListener('mousemove', e => {
  const rect = e.currentTarget.getBoundingClientRect();
  e.currentTarget.style.background = `radial-gradient(700px at ${e.clientX-rect.left}px ${e.clientY-rect.top}px, rgba(212, 163, 115,0.05), transparent 70%)`;
});
