import json


class result:

    def __init__(self, fistname, lastname, year_of_birth, gender, club=None, city=None, time=None, disqualification=None):
        self.fistname = fistname
        self.lastname = lastname,
        self.year_of_birth = int(year_of_birth)
        self.gender = gender
        self.club = {"club": club, "city": city}
        self.time = time
        self.disqualification = disqualification

    def get_attributes(self):
        keys = ["fistname", "lastname", "year_of_birth", "gender", "club", "time", "disqualification"]
        values = [self.fistname,
                  self.lastname,
                  self.year_of_birth,
                  self.gender,
                  self.club,
                  self.time,
                  self.disqualification]
        return dict.fromkeys(keys, values)


class event:

    def __init__(self, title, location, date):
        self.title = title
        self.location = location
        self.date = date

    def get_attributes(self):
        keys = ["title", "location", "date"]
        values = [self.title, self.location, self.date]
        return dict.fromkeys(keys, values)

class pool:

    def __init__(self, title, size):
        self.title = title
        self.size = size

    def get_attributes(self):
        return {"title": self.title, "size": self.size}


class competition:

    def __init__(self, event, pool, category, style, distance, results=None):
        self.event = event
        self.pool = pool
        self.category = category
        self.discipline = {"style": style, "distance": distance}
        self.results = [] if results is None else results

    def add_result(self, result):
        self.results.append(result)

    def get_attributes(self):
        results = [ res.get_attributes() for res in self.results]
        keys = ["event", "pool", "category", "discipline", "results"]
        values = [self.event.get_attributes(),
                  self.pool.get_attributes(),
                  self.category,
                  self.discipline,
                  results]
        return dict.fromkeys(keys, values)

    def save_json(self, file_name=None):
        if file_name is None:
            file_name = "{} {} {}".format(self.category, self.discipline["style"], self.discipline["distance"])
        with open(str(file_name) + ".json", "w") as write_file:
            json.dump(self.get_attributes(), write_file)


