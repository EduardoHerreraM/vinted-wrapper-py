class Item:

    def __init__(self, item_data):
        self.id = item_data.get('id')
        self.title = item_data.get('title')
        self.description = item_data.get('description')
        self.size = item_data.get('size')
        self.brand = item_data.get('brand')
        self.currency = item_data.get('currency')
        self.price_numeric = item_data.get('price_numeric')
        self.created_at_ts = item_data.get('created_at_ts')
        self.updated_at_ts = item_data.get('updated_at_ts')
        self.photos = [photo['full_size_url'] for photo in item_data.get('photos', [])]
        self.city = item_data.get('city')
        self.country = item_data.get('country')
        self.status_id = item_data.get('status_id')