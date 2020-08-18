class MenuItem:

    # メソッド（＝クラスの中で定義した関数）
    # __init__メソッドは、「クラス名()」でインスタンスを生成した直後に自動で呼び出される
    # インスタンスを生成すると同時にインスタンス変数に値を代入可能
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count

        if count >= 3:
            total_price *= 0.9

        return round(total_price)
