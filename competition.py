import json


class Result:

    def __init__(self, lastname, fistname, year_of_birth, gender, **kwargs):
        self.fistname = fistname
        self.lastname = lastname
        self.year_of_birth = int(year_of_birth)
        self.gender = gender
        club = kwargs["club"] if "club" in kwargs else None
        city = kwargs["city"] if "city" in kwargs else None
        self.club = {"club": club, "city": city}
        self.time = kwargs["time"] if "time" in kwargs else None
        self.disqualification = kwargs["disqualification"] if "disqualification" in kwargs else None
        self.rang = kwargs["rang"] if "rang" in kwargs else None

    def get_attributes(self):
        keys = ["fistname", "lastname", "year_of_birth", "gender", "club", "time", "disqualification", "rang"]
        values = [self.fistname,
                  self.lastname,
                  self.year_of_birth,
                  self.gender,
                  self.club,
                  self.time,
                  self.disqualification,
                  self.rang]
        return {key: value for (key, value) in zip(keys, values)}


class Event:

    def __init__(self, title, location, date):
        self.title = title
        self.location = location
        self.date = date

    def get_attributes(self):
        return {"title": self.title, "location": self.location, "date": self.date}

class Pool:

    def __init__(self, title, size):
        self.title = title
        self.size = size

    def get_attributes(self):
        return {"title": self.title, "size": self.size}


class Competition:

    def __init__(self, event, pool, category, style, distance, results=None):
        self.event = event
        self.pool = pool
        self.category = category
        self.discipline = {"style": style, "distance": distance}
        self.results = [] if results is None else results

    def add_result(self, result):
        self.results.append(result)

    def get_attributes(self):
        results = [ result.get_attributes() for result in self.results]
        keys = ["event", "pool", "category", "discipline", "results"]
        values = [self.event.get_attributes(),
                  self.pool.get_attributes(),
                  self.category,
                  self.discipline,
                  results]
        return {key: value for (key, value) in zip(keys, values)}

    def save_json(self, file_name=None):
        if file_name is None:
            file_name = "{} {} {}".format(self.category, self.discipline["style"], self.discipline["distance"])
        with open(str(file_name) + ".json", "w", encoding="utf-8") as write_file:
            json.dump(self.get_attributes(), write_file, sort_keys=False, indent=4,
                      ensure_ascii=False)

