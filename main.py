import requests
import os
from os import listdir
from os.path import isfile, join
from PIL import Image
from fpdf import FPDF
pdf = FPDF()


scans_url = "https://scansmangas.xyz/scans/"

print("---------------------------\nWelcome to a random manga downloader!\n")
manga_clear = input("Manga name: ")  # "kimetsu no yaiba"
manga = manga_clear.lower().replace(" ", "-")
first_chapter = input("First Chapter: ")
last_chapter = input("Last Chapter: ")

#manga_url = goodnoot_url + manga + "/chapters/chapitre-" + str(chapter) + "/"

# url = manga_url + str(page).zfill(2) + ".png"
manga_path = os.getcwd().replace("\\", "/") + \
    "/downloads/"+manga+"/"
#chapter_path = manga_path + str(chapter)


def getChapter(chapter):
    page = 1
    manga_url = scans_url + manga + "/" + str(chapter) + "/"
    chapter_path = manga_path + str(chapter)

    if os.path.exists(manga_path) == False:
        os.mkdir(manga_path)
    if os.path.exists(chapter_path) == False:
        os.mkdir(chapter_path)

    while True:
        #print("go page "+str(page))
        url = manga_url + str(page) + ".jpg"
        outfile = "downloads/"+manga+"/" + \
            str(chapter)+"/"+str(page)+".jpg"

        r = requests.get(url)
        if r.status_code == 200:
            with open(outfile, 'wb') as f:
                f.write(r.content)
                print("Downloaded page "+str(page))
                page += 1

        elif r.status_code == 404:
            break
    print('Done!')


'''     print("Generating PDF")

    files = [f for f in listdir(
        chapter_path) if isfile(join(chapter_path, f))]
    images = []
    for file in files:
        images.append(Image.open(chapter_path + "/" + file))

    pdf_path = manga_path + chapter + ".pdf"

    for image in files:
        pdf.add_page()
        pdf.image(chapter_path + "/" + image, 0, 0, 955, 1400)
    pdf.output(pdf_path, "F") '''


chapters = [i for i in range(int(first_chapter), int(last_chapter)+1)]
print(chapters)

for chapter in chapters:
    print("Getting chapter number "+str(chapter))
    getChapter(chapter)

print("Everything is now done,\nBye :)")
