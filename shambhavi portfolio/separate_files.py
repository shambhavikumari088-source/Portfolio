import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract CSS
style_start = html.find('<style>')
style_end = html.find('</style>')

if style_start != -1 and style_end != -1:
    css_content = html[style_start + len('<style>'):style_end]
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content.strip() + '\n')
    
    html = html[:style_start] + '<link rel="stylesheet" href="style.css">' + html[style_end + len('</style>'):]

# Extract JS
script_start = html.find('<script>')
script_end = html.rfind('</script>')

if script_start != -1 and script_end != -1:
    js_content = html[script_start + len('<script>'):script_end]
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js_content.strip() + '\n')
    
    html = html[:script_start] + '<script src="script.js"></script>' + html[script_end + len('</script>'):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Separation complete.")
