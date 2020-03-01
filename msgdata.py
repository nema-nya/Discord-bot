class MessageData:
    def __init__(self, manga_id, chapter, first_chapter, max_chapters, page, max_page, myEmbeded, pages = []):
        self.manga_id = manga_id
        self.chapter = chapter
        self.first_chapter = first_chapter
        self.max_chapters = max_chapters
        self.page = page
        self.max_page = max_page
        self.myEmbeded = myEmbeded
        self.pages = pages
    def __repr__(self):
        return f"MessageData({self.manga_id},{self.chapter},{self.first_chapter},{self.max_chapters},{self.page},{self.max_page},{self.pages})"

