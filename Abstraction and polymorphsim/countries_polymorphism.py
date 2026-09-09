class India():
    def capital(self):
        print("new delhi is the capital city of india")

    def language(self):
        print("hindi is the most widely spoken language in india")

    def economy(self):
        print("india is a developing country")



class USA():
    def capital(self):
        print("washington, D.C. is the capital city of USA")
    def language(self):
        print("english is the primary language of USA")
    def economy(self):
        print("USA is a develped country")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.economy()
