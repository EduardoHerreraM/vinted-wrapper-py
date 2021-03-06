from vinted_wrapper import settings as st
from vinted_wrapper.items.item import Item
from vinted_wrapper.requester import requester


class Items:

    @staticmethod
    def search_items(search_text, catalog_ids=None, color_ids=None, brand_ids=None, size_ids=None, material_ids=None,
                     status_ids=None, country_ids=None, city_ids=None, is_for_swap=0, page=1, per_page=24):
        """
        Perform a search operation in Vinted.
        :param search_text: str
        :param catalog_ids: list of ints
        :param color_ids: list of ints
        :param brand_ids: list of ints
        :param size_ids: list of ints
        :param material_ids: list of ints
        :param status_ids: list of ints
        :param country_ids: list of ints
        :param city_ids: list of ints
        :param is_for_swap: int
        :param page: int
        :param per_page: int
        :return:

        ---
        Note: I've not tested all the params, and many requires specific ids that I've not found out yet.
        """
        url = f'{st.VINTED_API_URL}/{st.VINTED_PRODUCTS_ENDPOINT}'
        params = {
            'search_text': search_text,
            'catalog_ids': ','.join(map(str, catalog_ids)) if catalog_ids else None,
            'color_ids': ','.join(map(str, color_ids)) if color_ids else None,
            'brand_ids': ','.join(map(str, brand_ids)) if brand_ids else None,
            'size_ids': ','.join(map(str, size_ids)) if size_ids else None,
            'material_ids': ','.join(map(str, material_ids)) if material_ids else None,
            'status_ids': ','.join(map(str, status_ids)) if status_ids else None,
            'country_ids': ','.join(map(str, country_ids)) if country_ids else None,
            'city_ids': ','.join(map(str, city_ids)) if city_ids else None,
            'is_for_swap': is_for_swap,
            'page': page,
            'per_page': per_page
        }
        data = requester.get(url=url, params=params)
        items = data.get('items', [])

        return [Item(_item) for _item in items]
