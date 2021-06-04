from vinted_wrapper import settings as st
from vinted_wrapper.items.item import Item
from vinted_wrapper.requester import requester


class Items:

    @staticmethod
    def search_items(search_text, catalog_ids=None, color_ids=None, brand_ids=None, size_ids=None, material_ids=None,
                     status_ids=None, country_ids=None, city_ids=None, is_for_swap=0, page=1, per_page=24):

        url = f'{st.VINTED_API_URL}/{st.VINTED_PRODUCTS_ENDPOINT}'
        params = {
            'search_text': search_text,
            'catalog_ids': catalog_ids,
            'color_ids': color_ids,
            'brand_ids': brand_ids,
            'size_ids': size_ids,
            'material_ids': material_ids,
            'status_ids': status_ids,
            'country_ids': country_ids,
            'city_ids': city_ids,
            'is_for_swap': is_for_swap,
            'page': page,
            'per_page': per_page
        }
        data = requester.get(url=url, params=params)
        items = data.get('items', [])

        return [Item(_item) for _item in items]
