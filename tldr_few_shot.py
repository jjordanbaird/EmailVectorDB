system_message = """Your goal is to clean up the text in this email newsletter. It will have \r and \n all over it that should be removed. 
The other thing you need to do is split the text into sections. 
This newsletter is structured usually in the following way:
- Title/headline (and usually a link)
- Short description
You should output these sections a list of dictionaries. {title: "Title", description: "description", links: ["link", "link"]}"""

example_in = """\r\n\r\nMISCELLANEOUS\r\n\r\nTSMC: SEMICONDUCTORS AND BORDERS OF LIGHT (25 MINUTE READ)\r\n[https://www.generalist.com/briefing/tsmc?utm_source=tldrnewsletter] \r\n\r\nTaiwan Semiconductor Manufacturing Company (TSMC) is one of the\r\nworld's most important companies. It makes chips for everything from\r\nphones to weapon systems. TSMC recently announced that it will\r\nincrease its financing for facilities in Arizona 
to $40 billion. The\r\nsemiconductor supply chain has many nearly irreplaceable players. Chip\r\nsanctions could be a potent weapon in the US and China's economic war.\r\n\r\n\r\nCHROME, 10 YEARS LATER (17 MINUTE READ)\r\n[https://neugierig.org/software/blog/2022/12/chrome.html?utm_source=tldrnewsletter]\r\n\r\n\r\nChrome, the web browser developed by Google, has more than 2.5 billion\r\nusers. This article discusses the reason for Chrome's creation, what\r\nit was like working on the project, the challenges of building a\r\nbrowser on Linux, and the impact of Chrome on the web. Chrome was\r\ncreated because Google wanted the web to succeed while having more\r\ninfluence over the product. \r\n\r\n"""

example_out = """[
    {
        "title": "TSMC: SEMICONDUCTORS AND BORDERS OF LIGHT (25 MINUTE READ)",
        "description": "Taiwan Semiconductor Manufacturing Company (TSMC) is one of the world's most important companies. It makes chips for everything from phones to weapon systems. TSMC recently announced that it will increase its financing for facilities in Arizona to $40 billion. The semiconductor supply chain has many nearly irreplaceable players. Chip sanctions could be a potent weapon in the US and China's economic war.",
        "links": ["https://www.generalist.com/briefing/tsmc?utm_source=tldrnewsletter"]
    },
    {
        "title": "CHROME, 10 YEARS LATER (17 MINUTE READ)",
        "description": "Chrome, the web browser developed by Google, has more than 2.5 billion users. This article discusses the reason for Chrome's creation, what it was like working on the project, the challenges of building a browser on Linux, and the impact of Chrome on the web. Chrome was created because Google wanted the web to succeed while having more influence over the product.",
        "links": ["https://neugierig.org/software/blog/2022/12/chrome.html?utm_source=tldrnewsletter"]
    }
]"""

