
from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    text = blocks.TextBlock(required=True)

    class Meta:
        template = "steams/title_and_text_block.html"
        icon="edit"
        label ="Title & Text"

class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template = "steams/richtext_block.html"
        icon="edit"
        label ="Full RichText"

class SimpleTextBlock(blocks.RichTextBlock):
    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]
    class Meta:
        template = "steams/richtext_block.html"
        icon="edit"
        label ="Simple RichText"

class NAVBAR(blocks.StructBlock):
    title = blocks.TextBlock(required=True)
    site1 = blocks.TextBlock(required=True)
    site2 = blocks.TextBlock(required=True)
    site3 = blocks.TextBlock(required=True)
    site4 = blocks.TextBlock(required=True)

    class Meta:
        template = "steams/NAVBAR.html"
        icon="edit"
        label ="NAVBAR"

class MASTERHEAD(blocks.StructBlock):
    HEADER = blocks.TextBlock(required=True)
    SUBTITLE = blocks.TextBlock(required=True)
    BUTTON = blocks.TextBlock(required=True)

    class Meta:
        template = "steams/MASTERHEAD.html"
        icon="edit"
        label ="MASTERHEAD"

class ABOUT(blocks.StructBlock):
    HEADER = blocks.TextBlock(required=True)
    SUBTITLE = blocks.TextBlock(required=True)
    BUTTON = blocks.TextBlock(required=True)

    class Meta:
        template = "steams/ABOUT.html"
        icon="edit"
        label ="ABOUT"