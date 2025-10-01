import feedparser

rss_url = 'docs/important.rdf'
feed = feedparser.parse(rss_url)

html = '<html><head><meta charset="UTF-8"><title>RSS一覧</title></head><body>'
html += '<h1>RSS一覧</h1><ul>'

for entry in feed.entries:
    html += f'<li>{entry.link}{entry.title}</a> ({entry.published})</li>'

html += '</ul></body></html>'

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
