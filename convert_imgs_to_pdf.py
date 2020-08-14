from PIL import Image
import glob
import logging
from os.path import isdir

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def imgs_to_pdf(folder_path, pdf_file_name='imgs_to_pdf.pdf'):

    if not isdir(folder_path):

        raise FileNotFoundError('The input folder does not exist.')

    imgs = glob.glob(f'{folder_path}/*.jpg')

    logging.info(f'Found {len(imgs)} images')

    imgs = list(
        map(
            lambda im: Image.open(im),
            imgs
        )
    )

    rotated_images = []

    for img in imgs:

        is_ok = False

        while not is_ok:

            img.show()

            inp = input('Rotate image? Y/N: ')

            if inp == 'Y':

                img = img.rotate(-90, expand=True)

            elif inp == 'N':

                rotated_images.append(img)

                is_ok = True

            else:

                print('Please, type Y or N.')

    logging.info('Saving pdf file...')

    rotated_images[0].save(f'{folder_path}/{pdf_file_name}', "PDF",
                           resolution=100.0,
                           save_all=True, append_images=rotated_images[1:])
