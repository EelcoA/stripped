import markdown

def convert_changelog_to_html(data):
    with open('CHANGELOG.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    with open('templates/changelog.html', 'w') as f:
        f.write(html)