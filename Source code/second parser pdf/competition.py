import json
import os


class Result:

    def __init__(self, last_name, first_name, birth_year, gender, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = int(birth_year)
        self.gender = gender
        self.club_name = kwargs["club_name"] if "club_name" in kwargs else None
        self.club_city = kwargs["club_city"] if "club_city" in kwargs else None
        self.club_country = kwargs["club_country"] if "club_country" in kwargs else None
        self.start_rank = kwargs["start_rank"] if "start_rank" in kwargs else None
        self.result_time = kwargs["result_time"] if "result_time" in kwargs else None
        self.dsq = kwargs["dsq"] if "dsq" in kwargs else None
        self.reason = kwargs["reason"] if "reason" in kwargs else None  # причина дисквалификации
        self.duration = kwargs["duration"] if "duration" in kwargs else None  # продолжительность дисквалификации

    def get_attributes(self):
        keys = ["first_name",
                "last_name",
                "birth_year",
                "gender",
                "club_name",
                "club_city",
                "club_country",
                "start_rank",
                "result_time",
                "dsq",
                "reason",
                "duration"]
        values = [self.first_name,
                  self.last_name,
                  self.birth_year,
                  self.gender,
                  self.club_name,
                  self.club_city,
                  self.club_country,
                  self.start_rank,
                  self.result_time,
                  self.dsq,
                  self.reason,
                  self.duration]
        return {key: value for (key, value) in zip(keys, values)}


class Record():

    def __init__(self, **kwargs):
        self.first_name = kwargs['first_name'] if 'first_name' in kwargs else None
        self.last_name = kwargs['last_name'] if 'last_name' in kwargs else None
        self.birth_year = kwargs['birth_year'] if 'birth_year' in kwargs else None
        self.gender = kwargs['gender'] if 'gender' in kwargs else None
        self.club_name = kwargs['club_name'] if 'club_name' in kwargs else None
        self.club_city = kwargs['club_city'] if 'club_city' in kwargs else None
        self.club_country = kwargs['club_country'] if 'club_country' in kwargs else None
        self.start_rank = kwargs['start_rank'] if 'start_rank' in kwargs else None
        self.record_time = kwargs['record_time'] if 'record_time' in kwargs else None
        self.record_date = kwargs['record_date'] if 'record_date' in kwargs else None

    def get_attributes(self):
        keys = ["first_name",
                "last_name",
                "birth_year",
                "gender",
                "club_name",
                "club_city",
                "club_country",
                "start_rank",
                "record_time",
                "record_date"]
        values = [self.first_name,
                  self.last_name,
                  self.birth_year,
                  self.gender,
                  self.club_name,
                  self.club_city,
                  self.club_country,
                  self.start_rank,
                  self.record_time,
                  self.record_date]
        return {key: value for (key, value) in zip(keys, values)}


class Competition:

    def __init__(self, **kwargs):
        self.comp_date = kwargs['comp_date'] if 'comp_date' in kwargs else None
        self.comp_city = kwargs['comp_city'] if 'comp_city' in kwargs else None
        self.comp_country = kwargs['comp_country'] if 'comp_country' in kwargs else None
        self.comp_chief_judge = kwargs['comp_chief_judge'] if 'comp_chief_judge' in kwargs else None
        self.comp_chief_secretary = kwargs['comp_chief_secretary'] if 'comp_chief_secretary' in kwargs else None
        style = kwargs['style'] if 'style' in kwargs else None
        distance = int(kwargs['distance']) if 'distance' in kwargs else None
        self.discipline = {'style': style, 'distance': distance}
        group_name = kwargs['group_name'] if 'group_name' in kwargs else None
        group_gender = kwargs['group_gender'] if 'group_gender' in kwargs else None
        self.group = {'name': group_name, 'gender': group_gender}
        self.record = kwargs['record'].get_attributes() if 'record' in kwargs else Record()
        self.result = kwargs['result'] if 'result' in kwargs else []

    def add_result(self, result):
        self.result.append(result)

    def get_attributes(self):
        results = [ result.get_attributes() for result in self.result]
        keys = ["comp_date",
                "comp_city",
                "comp_country",
                "comp_chief_judge",
                "comp_chief_secretary",
                "discipline",
                "group",
                "record",
                "result"]
        values = [self.comp_date,
                  self.comp_city,
                  self.comp_country,
                  self.comp_chief_judge,
                  self.comp_chief_secretary,
                  self.discipline,
                  self.group,
                  self.record.get_attributes(),
                  results]
        return {key: value for (key, value) in zip(keys, values)}



class Event:

    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else None
        self.description = kwargs['description'] if 'description' in kwargs else ''
        self.stage = kwargs['stage'] if 'stage' in kwargs else None
        self.competition = kwargs['competition'] if 'competition' in kwargs else []
        self.save_one_swim = kwargs['save_format'] if 'save_format' in kwargs else True
        self.save_dir = kwargs['save_dir'] if 'save_dir' in kwargs else 'jsons'

    def get_attributes(self, index_comp=-1):  # если не указать index_comp, то вернет весь список заплывов
        keys = ['name', 'description', 'stage', 'competition']
        if index_comp < 0:
            comp = [competition.get_attributes() for competition in self.competition]
        else:
            comp = [self.competition[index_comp].get_attributes()]
        values = [self.name, self.description, self.stage, comp]
        return {key: value for (key, value) in zip(keys, values)}

    def save_json(self, pool):
        if not os.path.isdir(self.save_dir):
            os.makedirs(self.save_dir)
        if self.save_one_swim:
            for i in range(len(self.competition)):
                file_name = "{}/stage {} {} {} {} {}.json".format(self.save_dir,
                                                                  self.stage,
                                                                  self.competition[i].discipline['distance'],
                                                                  self.competition[i].discipline['style'],
                                                                  self.competition[i].group['gender'],
                                                                  self.competition[i].group['name'])
                comp = {'event': self.get_attributes(i), 'pool': pool.get_attributes()}
                with open(file_name, "w", encoding="utf-8") as write_file:
                    json.dump(comp, write_file, sort_keys=False, indent=4, ensure_ascii=False)
        else:
            file_name = "{}/stage {}.json".format(self.save_dir, self.stage)
            event = {'event': self.get_attributes(), 'pool': pool.get_attributes()}
            with open(file_name, "w", encoding="utf-8") as write_file:
                json.dump(event, write_file, sort_keys=False, indent=4, ensure_ascii=False)


class Pool:

    def __init__(self, **kwargs):
        self.pool_name = kwargs['pool_name'] if 'pool_name' in kwargs else None
        self.pool_city = kwargs['pool_city'] if 'pool_city' in kwargs else None
        self.pool_country = kwargs['pool_country'] if 'pool_country' in kwargs else None
        self.pool_size = int(kwargs['pool_size']) if 'pool_size' in kwargs else None

    def get_attributes(self):
        return {'pool_name': self.pool_name, 'pool_city': self.pool_city, 'pool_country': self.pool_country,
                'pool_size': self.pool_size}
