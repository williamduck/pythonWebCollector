from PIL import Image
import subprocess

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    # Filter the image with a edge value, then save it.
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)

    # Call "tesseract" to OCR.
    subprocess.call(["tesseract", newFilePath, "output"])

    # Load the text result.
    outputFile = open("output.txt", 'r')
    print(outputFile.read())
    outputFile.close()

cleanFile("text_2.jpg", "text_2_clean.png")