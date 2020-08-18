from menu_item import MenuItem


class Food(MenuItem):

    # 親クラスのメソッドと同名メソッドを子クラスで定義 -> メソッド上書き(オーバーライド)
    # 子クラスで定義したメソッドを呼び出す
    # オーバーライドしたメソッド中で「super()」 -> 親クラスを呼び出せる
    # super().メソッド名() -> 親クラス内インスタンスメソッドを利用可能
    def __init__(self, name, price, calorie):
        super().__init__(name, price)
        self.calorie = calorie

    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'

    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')
