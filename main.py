from convert_imgs_to_pdf import imgs_to_pdf
import logging
import fire

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(folder_path: str, pdf_file_name: str = 'imgs_to_pdf.pdf'):
    """
    Command line application to convert a set of jpg images to pdf.
    :param folder_path: Folder of the images.
    :param pdf_file_name: Name of the output pdf. 
    """

    logging.info(f'Loading and converting images located in: {folder_path}')

    imgs_to_pdf(folder_path, pdf_file_name)

    logging.info(f'Images saved in {folder_path}\\{pdf_file_name}.')


if __name__ == '__main__':

    fire.Fire({
        'images_to_pdf': main,
    })
