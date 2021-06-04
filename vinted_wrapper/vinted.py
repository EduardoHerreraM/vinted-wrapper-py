import requests

from vinted_wrapper import settings as st
from vinted_wrapper.items import Items
from vinted_wrapper.requester import requester


class Vinted:

    def __init__(self):

        requester.set_cookie(url=st.VINTED_URL)
        self.items = Items()
