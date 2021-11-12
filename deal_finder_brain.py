import requests

LIST_OF_GAMES_ENDPOINT = "https://www.cheapshark.com/api/1.0/games"
LIST_OF_DEALS_ENDPOINT = "https://www.cheapshark.com/api/1.0/deals"


class DealFinderBrain:
    # Class for getting deals etc.
    def __init__(self):
        self.data_games = None
        self.data_deals = None
        self.game_list = []
        self.range = 10

    def get_list_of_games(self, name: str):
        params = {
            "title": name,
            "pageSize": self.range,
        }
        self.data_games = requests.get(url=LIST_OF_GAMES_ENDPOINT, params=params).json()
        return self.data_games

    def get_list_of_deals(self, steam_app_id: str):
        params = {
            "storeID": "1",
            "steamAppID": steam_app_id,
        }
        self.data_deals = requests.get(url=LIST_OF_DEALS_ENDPOINT, params=params).json()
        return self.data_deals

    def get_deals_for_game(self, name_of_game):
        for i in range(self.range):
            try:
                game_appid = self.get_list_of_games(name_of_game)[i]["steamAppID"]
                if game_appid is not None:
                    game_name = self.get_list_of_games(name_of_game)[i]["external"]
                    game_price_lowest = self.get_list_of_games(name_of_game)[i]["cheapest"]
                    is_on_sale = self.get_list_of_deals(game_appid)[0]["isOnSale"]
                    regular_price = self.get_list_of_deals(game_appid)[0]["normalPrice"]
                    sale_price = self.get_list_of_deals(game_appid)[0]["salePrice"]
                    if is_on_sale == "0":
                        result = f"""{game_name}, cheapest price was {game_price_lowest}, Game is not on sale, price is {regular_price}, link: https://store.steampowered.com/app/{game_appid} """

                        # print(result)
                    elif is_on_sale == "1":
                        result = f"""{game_name}, cheapest price was {game_price_lowest}, Game is on sale! Sale price is {sale_price}, link: https://store.steampowered.com/app/{game_appid} """
                        self.game_list.append(result)
                        # print(result)
                else:
                    pass
            except IndexError:
                pass
        return self.game_list

