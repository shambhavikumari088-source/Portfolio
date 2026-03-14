import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace css vars
content = content.replace(
""":root {
  --bg: #faf3ee; /* Light Cream Background */
  --bg2: #f4eae1; /* Slightly darker cream */
  --cyan: #8c6b54; /* Medium Brown for primary accents */
  --teal: #a68c78; /* Muted Brown */
  --violet: #c89f7f; /* Warm Tan */
  --pink: #d6b89e; /* Light Tan */
  --lime: #8c6b54; /* Medium Brown */
  --white: #241c18; /* Dark Brown replacing white for readability */
  --muted: #a68c78; /* Muted Brown */
  --glass: rgba(140, 107, 84, 0.05); /* Brown glass */
  --glass-border: rgba(140, 107, 84, 0.15);
}""",
""":root {
  --bg: #0a0807; /* Almost Black */
  --bg2: #16110d; /* Very Dark Brown */
  --cyan: #d4a373; /* Creamy Brown Accent */
  --teal: #a47d52; /* Muted Brown */
  --violet: #eaddcf; /* Cream */
  --pink: #faedcd; /* Light Cream */
  --lime: #8b6038; /* Darker Brown */
  --white: #fefae0; /* Creamy White text */
  --muted: #8e7d70; /* Muted Brown */
  --glass: rgba(212, 163, 115, 0.05); /* Brown glass */
  --glass-border: rgba(212, 163, 115, 0.15);
}"""
)

# Colors
content = content.replace('rgba(140, 107, 84,', 'rgba(212, 163, 115,')
content = content.replace('rgba(0,245,212,', 'rgba(212, 163, 115,')
content = content.replace('rgba(123,47,255,', 'rgba(234, 221, 207,')
content = content.replace('rgba(255,45,155,', 'rgba(250, 237, 205,')
content = content.replace('rgba(214, 184, 158,', 'rgba(212, 163, 115,')
content = content.replace('color: #5a9aaa;', 'color: var(--muted);')

content = content.replace(
"""body::after {
  content: '';
  position: fixed; inset: 0; z-index: 1; pointer-events: none;
  background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(212, 163, 115, 0.05) 2px, rgba(212, 163, 115, 0.05) 4px); /* Light grid lines */
}""",
"""body::after {
  content: '';
  position: fixed; inset: 0; z-index: 1; pointer-events: none;
  background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(212, 163, 115, 0.03) 2px, rgba(212, 163, 115, 0.03) 4px); /* Light grid lines */
}"""
)

content = content.replace("mix-blend-mode: difference; /* Changed from screen for light mode */", "mix-blend-mode: screen;")
content = content.replace("background: rgba(250, 243, 238, 0.85); /* Light translucent nav */", "background: rgba(10, 8, 7, 0.85);")


content = content.replace(
"""/* HERO IMAGE PLACEHOLDER */
.hero-image-placeholder {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: var(--bg2);
  border: 2px dashed rgba(212, 163, 115, 0.4);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 2rem;
  color: var(--cyan);
  position: relative;
  z-index: 10;
  animation: fadeSlideUp 0.8s ease both;
  box-shadow: 0 10px 30px rgba(212, 163, 115, 0.1);
  overflow: hidden;
}
.hero-image-placeholder i {
    font-size: 40px;
    margin-bottom: 8px;
    color: rgba(212, 163, 115, 0.6);
}""",
"""/* HERO IMAGE PLACEHOLDER */
.hero-image-placeholder {
  width: 380px;
  height: 380px;
  border-radius: 12px;
  background: var(--bg2);
  border: 1px solid var(--glass-border);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 0;
  color: var(--cyan);
  position: relative;
  z-index: 10;
  animation: fadeSlideUp 0.8s ease both;
  box-shadow: 0 20px 50px rgba(0,0,0,0.5), inset 0 0 30px rgba(212,163,115,0.05);
  overflow: hidden;
}
.hero-image-placeholder i {
    font-size: 60px;
    margin-bottom: 12px;
    color: rgba(212,163,115,0.6);
}"""
)

content = content.replace(
""".profile-pic-placeholder {
    width: 100%;
    aspect-ratio: 1;
    background: rgba(212, 163, 115, 0.05); /* Cyber theme */
    border: 2px dashed rgba(212, 163, 115, 0.3);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: var(--cyan);
    border-radius: 10px;
    overflow: hidden;
    position: relative;
}
.profile-pic-placeholder img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: none; /* hidden until an image is provided */
}
.profile-pic-placeholder i {
    font-size: 50px;
    margin-bottom: 10px;
    color: rgba(212, 163, 115, 0.5);
}""",
""".profile-pic-placeholder {
    width: 100%;
    aspect-ratio: 1;
    background: var(--glass);
    border: 1px solid var(--glass-border);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: var(--cyan);
    border-radius: 12px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 15px 40px rgba(0,0,0,0.5);
}
.profile-pic-placeholder img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: none;
}
.profile-pic-placeholder i {
    font-size: 50px;
    margin-bottom: 10px;
    color: rgba(212,163,115,0.5);
}"""
)

content = content.replace(
"""  <div class="hero-image-placeholder">
    <i class="fas fa-portrait"></i>
    <p style="font-size: 0.7rem; letter-spacing: 0.1em; font-family: 'Syne Mono', monospace;">Insert Picture</p>
  </div>
  <div class="glitch-badge"><div class="badge-dot"></div> Biotechnologist · Data Scientist · Builder</div>
  <h1 class="hero-name">
    <span class="line1">Shambhavi</span>
    <span class="line2">Kumari</span>
  </h1>
  <div class="hero-role">B.Tech Biotechnology · LPU · Class of 2027</div>
  <p class="hero-desc">Where pharmaceutical science meets computational intelligence — building bridges between wet lab precision and algorithmic thinking. From GMP cleanrooms to machine learning pipelines.</p>
  <div class="hero-ctas">
    <a href="#projects" class="btn-glow">Explore Work</a>
    <a href="SHAMBHAVI_KUMARI_CV.pdf" class="btn-glow btn-pink" target="_blank" onclick="alert('Attach your CV PDF to activate the download link.')">Download CV</a>
  </div>""",
"""  <div style="display: flex; align-items: center; justify-content: space-between; width: 100%; z-index: 10; gap: 4rem; flex-wrap: wrap-reverse;">
    <div style="flex: 1; min-width: 320px;">
      <div class="glitch-badge"><div class="badge-dot"></div> Biotechnologist · Data Scientist · Builder</div>
      <h1 class="hero-name">
        <span class="line1">Shambhavi</span>
        <span class="line2">Kumari</span>
      </h1>
      <div class="hero-role">B.Tech Biotechnology · LPU · Class of 2027</div>
      <p class="hero-desc">Where pharmaceutical science meets computational intelligence — building bridges between wet lab precision and algorithmic thinking. From GMP cleanrooms to machine learning pipelines.</p>
      <div class="hero-ctas">
        <a href="#projects" class="btn-glow">Explore Work</a>
        <a href="SHAMBHAVI_KUMARI_CV.pdf" class="btn-glow btn-pink" target="_blank" onclick="alert('Attach your CV PDF to activate the download link.')">Download CV</a>
      </div>
    </div>
    <div style="flex-shrink: 0; display: flex; justify-content: center;">
      <div class="hero-image-placeholder">
        <i class="fas fa-portrait"></i>
        <p style="font-size: 0.75rem; letter-spacing: 0.15em; font-family: 'Syne Mono', monospace;">INSERT PICTURE</p>
      </div>
    </div>
  </div>"""
)

content = content.replace(
"color: ['#d6b89e','#8c6b54','#ede0d4','#c89f7f'][Math.floor(Math.random()*4)],",
"color: ['#d4a373','#a47d52','#faedcd','#eaddcf'][Math.floor(Math.random()*4)],"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
