#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/5/17


class BaseWeChatClientAPI(object):

    """
    公众号调用的 基类API
    """

    def __init__(self, client=None):
        self._client = client

    def _get(self, url, **kwargs):
        if hasattr(self, "API_BASE_URL"):
            kwargs['api_base_url'] = getattr(self, "API_BASE_URL")
        return self._client.get(url, **kwargs)

    def _post(self, url, **kwargs):
        if hasattr(self, "API_BASE_URL"):
            kwargs['api_base_url'] = getattr(self, "API_BASE_URL")
        return self._client.post(url, **kwargs)

    @property
    def access_token(self):
        return self._client.access_token

    @property
    def app_id(self):
        return self._client.app_id
