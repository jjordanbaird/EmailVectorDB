class TLDRSplitter:
    """
    TLDRSplitter is a class to parse the body of the TLDR Newsletter emails.
    It splits the content into sections based on predefined delimiters.
    """ 
    def __init__(self) -> None:
        self.delimiters = [
            "Headlines & Launches",
            "Research & Innovation",
            "Engineering & Resources",
            "MISCELLANEOUS",
            "Quick Links",
            "Big Tech & Startups",
            "Science & Futuristic Technology",
            "Science & Futuristic Technology",
            "Programming, Design & Data Science",
            "DAILY UPDATE"
        ]

    def parse(self, body: str) -> list[str]:
        li = []
        for delimiter in self.delimiters:
            if body.lower().find(delimiter.lower()) != -1:
                li.append(body.lower().find(delimiter.lower()))
        li.sort()

        sections = []
        for i in range(len(li)):
            if i == len(li) - 1:
                sections.append(body[li[i]:])
            else:
                sections.append(body[li[i]:li[i+1]])

        return sections

