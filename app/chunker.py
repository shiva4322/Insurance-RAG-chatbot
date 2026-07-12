from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:

    def __init__(self, chunk_size=500, overlap=100):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                "! ",
                "? ",
                " ",
                ""
            ]
        )

    def chunk_text(self, text):
        return self.splitter.split_text(text)