from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.six import BytesIO
from PIL import Image, ImageDraw, ImageFont


class MyStorage(FileSystemStorage):
    font_path = '/Applications/Utilities/Console.app/Contents/Resources/Fonts/SFMono-Regular.otf'

    def save(self, name, content, max_length=None):
        if 'image' in content.content_type:
            # 加水印
            image = self.watermark_with_text(content, 'atlednolispe', 'green')
            content = self.convert_image_to_file(image, name)

        return super(MyStorage, self).save(name, content, max_length=max_length)

    def convert_image_to_file(self, image, name):
        temp = BytesIO()
        image.save(temp, format='PNG')
        return InMemoryUploadedFile(temp, None, name, 'image/png', None, None)

    def watermark_with_text(self, file_obj, text, color, fontfamily=font_path):
        image = Image.open(file_obj).convert('RGBA')
        imageWatermark = Image.new('RGBA', image.size, (255, 255, 255, 0))

        draw = ImageDraw.Draw(imageWatermark)
        width, height = image.size
        margin = 10
        font = ImageFont.truetype(fontfamily, int(height / 20))
        textWidth, textHeight = draw.textsize(text, font)
        x = (width - textWidth - margin) / 2
        y = height - textHeight - margin

        draw.text((x, y), text, color, font)

        return Image.alpha_composite(image, imageWatermark)