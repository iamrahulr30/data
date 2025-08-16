from html.parser import HTMLParser

class TextLinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)   # auto-unescape entities
        self._skip_tag = None                     # 'script' or 'style' when skipping
        self._current_href = None                 # href for current <a>
        self._pieces = []  
        self.tags = ("script", "style" , "nav" , "aside" , "footer" , "header")                       # collected text pieces

    def handle_starttag(self, tag, attrs):
        if tag in self.tags:
            self._skip_tag = tag
            return
        if tag == "a":
            for k, v in attrs:
                if k.lower() == "href" and v:
                    self._current_href = v
                    break

    def handle_endtag(self, tag):
        if tag == self._skip_tag:
            self._skip_tag = None
        if tag == "a":
            self._current_href = None

    def handle_data(self, data):
        if self._skip_tag :
            return
        text = " ".join(data.split())   # collapse whitespace
        if not text:
            return
        if self._current_href:
            self._pieces.append(f"{text} ({self._current_href})")
        else:
            self._pieces.append(text)

def extract_text_and_links() -> str:
    with open("content.html" , "r" , encoding = "utf-8") as f :
        html = f.read()
        p = TextLinkExtractor()
        p.feed(html)
        p.close()
        print(" ".join(p._pieces).strip())




