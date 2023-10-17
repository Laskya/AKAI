import json, datetime, urllib.request


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        today = datetime.date.today().strftime("%Y-%m-%d")
        file = open("ratios.json", "r")
        data = json.load(file)
        file.close()
        for i in data:
            if (
                i["base_currency"] == self.base
                and i["target_currency"] == self.target
                and i["date_fetched"] == today
            ):
                return True
        return False

    def fetch_ratio(self):
        # ACCES KEY !!!!!!!!!!
        bearer = "<ACCESS_KEY>"
        
        url = f"http://api.exchangerate.host/convert?access_key={bearer}&from={self.base}&to={self.target}&amount=1"
        # If you can afford subscription
        # url = f"https://api.exchangerate.host/convert?access_key={bearer}&from={self.base}&to={self.target}&amount=1"
        with urllib.request.urlopen(url) as response:
            body = response.read()
        data = json.loads(body)
        self.save_ratio(data["result"])
        pass

    def save_ratio(self, ratio):
        today = datetime.date.today().strftime("%Y-%m-%d")
        file = open("ratios.json", "r+")
        data = json.load(file)
        file.close()
        for i in data:
            if i["base_currency"] == self.base and i["target_currency"] == self.target:
                i["ratio"] = ratio
                i["date_fetched"] = today
                break
        else:
            data.append(
                {
                    "base_currency": self.base,
                    "target_currency": self.target,
                    "date_fetched": today,
                    "ratio": ratio,
                }
            )
        file = open("ratios.json", "w")
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.close()
        pass

    def get_matched_ratio_value(self):
        file = open("ratios.json", "r")
        data = json.load(file)
        file.close()
        for i in data:
            if i["base_currency"] == self.base and i["target_currency"] == self.target:
                return i["ratio"]
