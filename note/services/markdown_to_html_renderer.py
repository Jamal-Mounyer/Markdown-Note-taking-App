import markdown
import nh3

def markdown_renderer(text):
    html = markdown.markdown(text, extensions=["fenced_code", "tables"])
    
    safe_html = nh3.clean(
        html,
        tags={
            "h1", "h2", "h3", "h4", "h5", "h6",
            "p", "br",
            "strong", "em", "del",
            "ul", "ol", "li",
            "a", "blockquote",
            "pre", "code", "hr",
            "table", "thead", "tbody",
            "tr", "th", "td",
            "img",
        },
        attributes={
            "a": {"href", "title"},
            "img": {"src", "alt", "title"},
        },
    )
    
    return safe_html