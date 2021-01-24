import markdown

def convert_changelog_to_html(data):
    with open('CHANGELOG.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)


    with open('templates/changelog.html', 'w') as f:
        f.write("{ % extends '_base.html' %}")
        f.write("{ % load static %}")
        f.write("{ % block title %}NPO-RM Changelog { % endblock title %}")
        f.write("{ % block content %}")
        f.write("<div class='container-fluid pl-3'>")
        f.write("<br>")
        f.write(html)
        f.write("</div>")
        f.write("{% endblock content %}")
