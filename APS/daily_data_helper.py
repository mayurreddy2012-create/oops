class DailyDataHelper:
    def __init__(self):
        self.data = ["Math", "Science", "English"]
        print("Daily Data Helper started!")
    def show_data(self):
        print("Today's data:")
        for item in self.data:
            print(item)
    def search_data(self, search_item):
        for index, value in enumerate(self.data):
            if value == search_item:
                print("Found:", value)
                print("Index:", index)
                return
        print("Item not found.")
    def __del__(self):
        print("Daily Data Helper has ended.")
helper = DailyDataHelper()
helper.show_data()
helper.search_data("Science")