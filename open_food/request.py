import requests
from bs4 import BeautifulSoup


def get_link_products(page):
    """
    :param page: the number page of site open food.
    :return: The list with links the products or error message if the site open food is out.
    """
    try:
        url = f'https://world.openfoodfacts.org/'
        page_html = requests.get(url+str(page))
        content_html = BeautifulSoup(page_html.text, 'html.parser')
        list_links_product = list()
        for product in content_html.select('.row ul.products'):
            for p in product.select('a'):
                if 'href' in p.attrs:
                    list_links_product.append(url + str(p.attrs['href']))
        return list_links_product
    except ConnectionError as error:
        return error


if __name__ == '__main__':
    links = get_link_products(2)
    if isinstance(links, list):
        for number, link in enumerate(links):
            print(f'Produto {number+1}: {link}')
    else:
        print(links)
