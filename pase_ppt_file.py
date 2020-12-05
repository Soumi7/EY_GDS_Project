

from pptx import Presentation


prs = Presentation("/home/soumi/Downloads/EYintentRepository/Repository 1/Item 4/azure-250215.pptx")
print("----------------------")
for slide in prs.slides:
    for shape in slide.shapes:
        if hasattr(shape, "text"):
            print(shape.text)