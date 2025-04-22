import os
import requests

# Community Dragon base url
BASE_URL = "https://raw.communitydragon.org/latest/"

def read_urls_from_file(file_route):
    """
    Reads a text file with URLs and returns them as a list.
    """
    with open(file_route, "r") as fileToRead:
        return fileToRead.read().strip().split("\n")


def filter_urls(url_list, blacklist):
    """
    Filters URLs that do not contain any of the words in the blacklist
    and end in ".png".

    :param url_list: List of URLs to filter.
    :param blacklist: List of keywords to exclude.
    :return: List of filtered URLs.
    """
    return [
        url for url in url_list
        if all(BLkeyword not in url for BLkeyword in blacklist) and url.endswith(".png")
    ]


def download_asset(url, folder_destination="assets"):
    """
    Download a file from a URL and save it to the destination folder.
    """
    # Crear la carpeta de destino si no existe
    if not os.path.exists(folder_destination):
        os.makedirs(folder_destination)

    # Nombre del archivo a descargar
    file_name = os.path.basename(url)
    f_route = os.path.join(folder_destination, file_name)

    # Descargar el archivo
    try:
        response = requests.get(BASE_URL + url)
        response.raise_for_status()  # Verificar si la descarga fue exitosa

        # Guardar el archivo
        with open(f_route, "wb") as archivo:
            archivo.write(response.content)
        print(f"Downloading: {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error on {file_name}: {e}")


def download_assets_from_list(url_list, folder_destination="assets"):
    """
    Download all assets from a list of URLs.
    """
    for url in url_list:
        download_asset(url, folder_destination)

