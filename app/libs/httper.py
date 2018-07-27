import requests


class Http:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json

        # 方式一：这种方式耗费时间较长，做太多时间的判断
        # if r.status_code == 200:
        #     return r.json() if return_json else r.text
        # return {} if return_json else ''
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        #
        # 方式三：
        # if return_json:
        #     if r.status_code == 200:
        #         return r.json()
        #     else:
        #         return r.text
        # if return_json:
        #     if r.status_code != 200:
        #         return {}
        #     else:
        #         return ''

