import os


class EmptyApiKey(Exception):
    def __init__(self):
        super().__init__("Empty API key, Don't forget to \
add the OPENAI_API_KEY to your environment")


class Options():
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def init_options():
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        raise EmptyApiKey
    return Options(api_key=api_key)


init_options()
