import re


class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:
        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Remove leading/trailing whitespace
        text = text.strip()

        return text