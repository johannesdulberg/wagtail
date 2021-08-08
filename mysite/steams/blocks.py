from django.db import models
from django.db.models.deletion import SET_NULL

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
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
class NavbarCentered(blocks.StructBlock):
    title = blocks.TextBlock(required=True)
    site1 = blocks.TextBlock(required=True)
    site2 = blocks.TextBlock(required=True)
    site3 = blocks.TextBlock(required=True)
    site4 = blocks.TextBlock(required=True)

    class Meta:
        template = "steams/NavbarCentered.html"
        icon="edit"
        label ="NavbarCentered"
class MASTERHEAD(blocks.StructBlock):
    HEADER = blocks.TextBlock(required=True)
    SUBTITLE = blocks.TextBlock(required=True)
    BUTTON = blocks.TextBlock(required=False)
    MasterImage = ImageChooserBlock(required=True)

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

class SERVICES(blocks.StructBlock):
    HEADER = blocks.TextBlock(required=True)
    Service1Header = blocks.TextBlock(required=True)
    Service1Subtitle = blocks.TextBlock(required=True)
    Service2Header = blocks.TextBlock(required=True)
    Service2Subtitle = blocks.TextBlock(required=True)
    Service3Header = blocks.TextBlock(required=True)
    Service3Subtitle = blocks.TextBlock(required=True)
    Service4Header = blocks.TextBlock(required=True)
    Service4Subtitle = blocks.TextBlock(required=True)

    class Meta:
        template = "steams/SERVICES.html"
        icon="edit"
        label ="SERVICES"

class GALLERIE(blocks.StructBlock):
    Image1 = ImageChooserBlock(required=True)
    Image2 = ImageChooserBlock(required=True)
    Image3 = ImageChooserBlock(required=True)
    Image4 = ImageChooserBlock(required=True)
    Image5 = ImageChooserBlock(required=True)
    Image6 = ImageChooserBlock(required=True)
    Image1Thumbnail = ImageChooserBlock(required=True)
    Image2Thumbnail = ImageChooserBlock(required=True)
    Image3Thumbnail = ImageChooserBlock(required=True)
    Image4Thumbnail = ImageChooserBlock(required=True)
    Image5Thumbnail = ImageChooserBlock(required=True)
    Image6Thumbnail = ImageChooserBlock(required=True)
    Image1Categorie = blocks.TextBlock(required=True)
    Image1Project = blocks.TextBlock(required=True)
    Image2Categorie = blocks.TextBlock(required=True)
    Image2Project = blocks.TextBlock(required=True)
    Image3Categorie = blocks.TextBlock(required=True)
    Image3Project = blocks.TextBlock(required=True)
    Image4Categorie = blocks.TextBlock(required=True)
    Image4Project = blocks.TextBlock(required=True)
    Image5Categorie = blocks.TextBlock(required=True)
    Image5Project = blocks.TextBlock(required=True)
    Image6Categorie = blocks.TextBlock(required=True)
    Image6Project = blocks.TextBlock(required=True)

    class Meta:
        template = "steams/GALLERIE.html"
        icon="edit"
        label ="GALLERIE"

class SERVICES(blocks.StructBlock):
    HEADER = blocks.TextBlock(required=True)
    Service1Header = blocks.TextBlock(required=True)
    Service1Subtitle = blocks.TextBlock(required=True)
    Service2Header = blocks.TextBlock(required=True)
    Service2Subtitle = blocks.TextBlock(required=True)
    Service3Header = blocks.TextBlock(required=True)
    Service3Subtitle = blocks.TextBlock(required=True)
    Service4Header = blocks.TextBlock(required=True)
    Service4Subtitle = blocks.TextBlock(required=True)

    class Meta:
        template = "steams/SERVICES.html"
        icon="edit"
        label ="SERVICES"

class CONTACT(blocks.StructBlock):
    HEADER = blocks.TextBlock(required=True)
    headerSubtitle = blocks.TextBlock(required=True)
    button = blocks.TextBlock(required=True)
    

    class Meta:
        template = "steams/CONTACT.html"
        icon="edit"
        label ="CONTACT"

class VideoHeader(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    subtitle = blocks.TextBlock(required=True)
    BUTTON= blocks.TextBlock(required=False)

    class Meta:
        template = "steams/VideoHeader.html"
        icon="edit"
        label ="VideoHeader"

class CardPicture(blocks.StructBlock):
    title = blocks.TextBlock(required=True)
    subtitle = blocks.TextBlock(required=True)
    btn = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=True)
    position = blocks.TextBlock(required=False)

    class Meta:
        template = "steams/CardPicture.html"
        icon="edit"
        label ="CardPicture"

class ThreeImagesCallToAction(blocks.StructBlock):
    title1 = blocks.TextBlock(required=True)
    title2 = blocks.TextBlock(required=True)
    title3 = blocks.TextBlock(required=True)
    subtitle1 = blocks.TextBlock(required=True)
    subtitle2 = blocks.TextBlock(required=True)
    subtitle3 = blocks.TextBlock(required=True)
    info1 = blocks.TextBlock(required=True)
    info2 = blocks.TextBlock(required=True)
    info3 = blocks.TextBlock(required=True)
    btn1 = blocks.TextBlock(required=False)
    btn2 = blocks.TextBlock(required=False)
    btn3 = blocks.TextBlock(required=False)
    image1 = ImageChooserBlock(required=True)
    image2 = ImageChooserBlock(required=True)
    image3 = ImageChooserBlock(required=True)

    class Meta:
        template = "steams/ThreeImagesCallToAction.html"
        icon="edit"
        label ="ThreeImagesCallToAction"