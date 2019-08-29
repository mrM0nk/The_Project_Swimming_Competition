import json
import os
import re

from parser_class import Parser


class KaunasGrandPrixParser(Parser):

    def __init__(self):
        self.competition_area_pattern = re.compile(r'^[Ee]vent.+\n'
                                                   r'^\d{4}.+\n'
                                                   r'^[Pp]oints.+\n'
                                                   r'^\w.+\n', re.MULTILINE)
        self.page_delimiter_pattern1 = re.compile(r'^.+Page\s\d+\n(.+\n)*?^Event.+\n', re.MULTILINE)
        self.page_delimiter_pattern2 = re.compile(r'^.+Page\s+\d+\n(.+\n)*', re.MULTILINE)
        self.athelete_group_pattern = re.compile(r'^\d+.*years\b.*', re.MULTILINE)
        self.discipline_desc_pattern = re.compile(r'(\w+),\s+(\d\w?\d+)m\s+(\w+\b)')
        self.result_row_pattern = re.compile(r'((?:\w+[ -])?\w+),\s*(.+?)\s*(\d{2,4})\s+(.+?)(\d?:?\d+[.]\d{2})')
        self.dsq_row_pattern = re.compile(r'(^\w+)\s+((?:\w+[ -])?\w+),\s*(.+?)\s+(\d{2,4})\s+(.+)', re.MULTILINE)

    def get_stages(self):
        pass

    def get_competitions(self, data):
        competitions_list = re.findall(self.competition_area_pattern, data)
        competitions_results = re.split(self.competition_area_pattern, data)
        competitions_results = competitions_results[1:]
        return competitions_list, competitions_results

    def get_athlete_gender(self, text):
        gender_dictionary = {
            "m": ["boys", "men"],
            "f": ["girls", "women"]
        }
        gender = None
        if str.lower(text) in gender_dictionary["m"]:
            gender = "m"
        elif str.lower(text) in gender_dictionary["f"]:
            gender = "f"
        else:
            gender = text
        return gender

    def get_athlete_groups(self, area):
        groups_list = re.findall(self.athelete_group_pattern, area)
        group_results = re.split(self.athelete_group_pattern, area)[1:]
        return groups_list, group_results

    def get_results(self, rows):
        return re.findall(self.result_row_pattern, rows)

    def get_record_row(self):
        pass

    def get_result_time(self, time):
        match = re.findall(re.compile(r"(\d)?[:]?(\d{2})[.](\d{2})"), time)[0]
        return '00:' + match[0].rjust(2, '0') + ":" + match[1] + '.' + match[2]

    def get_competition_city(self, area):
        area = area.split('\n')
        return str.strip(area[1][0:area[1].index(',')])

    def get_competition_date(self, area):
        competition_date = area[1].split('-')
        competition_date = str.strip(competition_date[2]) + '.' + str.strip(competition_date[1]) + '.' + str.strip(
            competition_date[0])
        return competition_date

    def get_disqualifications(self, rows):
        return re.findall(self.dsq_row_pattern, rows)

    def get_event_name(self, area):
        return str.strip(area.split('\n')[0])

    def get_headers(self):
        pass

    def get_pool(self):
        pass

    def read_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def write_to_json(self, file_name, data):
        file_path = "./resources/json/{}".format(file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as output_file:
            json.dump(data, output_file, sort_keys=True, indent=4, ensure_ascii=False)

    def get_event_area(self, data):
        return re.split(self.competition_area_pattern, data)[0]

    def parse_files_from_directory(self):
        pass

    def parse_file(self, file_path):

        def delete_blank_lines(text_data):
            return text_data.replace("\n\n", "\n")

        def clean_results(text_data):
            results = re.sub(self.page_delimiter_pattern1, '', text_data, count=0)
            results = re.sub(self.page_delimiter_pattern2, '', results, count=0)
            results = delete_blank_lines(results)
            return results

        def convert_to_four_digit_year(year):
            result_year = ""
            year = str.strip(year)
            if len(year) == 2:
                if int(year) <= 50:
                    result_year = "2" + str.rjust(year, 3, "0")
                elif int(year) > 50:
                    result_year = "19" + year
            return int(result_year)

        json_root = {"event": None}
        event = {
            "name": "",
            "description": "",
            "stage": "",
            "competition": list(),
            "pool": None
        }
        pool = {
            "pool_name": "",
            "pool_city": "",
            "pool_country": "",
            "pool_size": None
        }
        data = self.read_data_from_file(file_path)
        data = delete_blank_lines(data)

        event_area = self.get_event_area(data)
        event["name"] = self.get_event_name(event_area)
        event_city = self.get_competition_city(event_area)

        competitions_list, competitions_areas_list = self.get_competitions(data)

        for ix in range(0, len(competitions_list)):
            competition = {
                "comp_date": "",
                "comp_city": "",
                "comp_country": "",
                "comp_chief_judge": "",
                "comp_chief_secretary": "",
                "discipline": dict(),
                "group": dict(),
                "record": dict(),
                "result": list()
            }
            discipline = {
                "style": "",
                "distance": None
            }
            group = {
                "name": "",
                "gender": ""
            }
            record = {
                "first_name": "",
                "last_name": "",
                "birth_year": "",
                "gender": "",
                "club_name": "",
                "club_city": "",
                "club_country": "",
                "start_rank": "",
                "record_time": "",
                "record_date": ""
            }

            competition_area = competitions_list[ix].split('\n')
            competition["comp_date"] = self.get_competition_date(competition_area)
            competition["comp_city"] = event_city

            discipline_description = re.findall(
                self.discipline_desc_pattern, competition_area[0])[0]
            # discipline_description=(group, distance, style)
            discipline["distance"] = discipline_description[1]
            discipline["style"] = discipline_description[2]

            gender = self.get_athlete_gender(discipline_description[0])

            results = clean_results(competitions_areas_list[ix])
            groups_list, groups_result_areas = self.get_athlete_groups(results)

            #   if groups don't exist
            # if len(groups_list) == 0 and results != "":
            #     groups_list.append("Unknown")
            #     groups_result_areas.append(results)

            for iy in range(0, len(groups_list)):
                group["name"] = groups_list[iy]
                group["gender"] = gender
                results_list = list()
                group_results = self.get_results(groups_result_areas[iy])
                group_dsq = self.get_disqualifications(groups_result_areas[iy])

                for row in group_results:
                    result = {
                        "first_name": "",
                        "last_name": "",
                        "birth_year": None,
                        "gender": "",
                        "club_name": "",
                        "club_city": "",
                        "club_country": "",
                        "start_rank": "",
                        "result_time": "",
                        "dsq": "",
                        "reason": "",
                        "duration": ""
                    }
                    result["first_name"] = row[0]
                    result["last_name"] = row[1]
                    result["birth_year"] = convert_to_four_digit_year(row[2])
                    result["club_name"] = ' '.join(row[3].split())
                    result["result_time"] = self.get_result_time(row[4])
                    result["gender"] = gender
                    results_list.append(result)

                for row in group_dsq:
                    result = {
                        "first_name": "",
                        "last_name": "",
                        "birth_year": None,
                        "gender": "",
                        "club_name": "",
                        "club_city": "",
                        "club_country": "",
                        "start_rank": "",
                        "result_time": "",
                        "dsq": "",
                        "reason": "",
                        "duration": ""
                    }
                    result["first_name"] = row[1]
                    result["last_name"] = row[2]
                    result["birth_year"] = convert_to_four_digit_year(row[3])
                    result["club_name"] = ' '.join(row[4].split())
                    result["dsq"] = row[0]
                    result["gender"] = gender
                    results_list.append(result)

                competition["discipline"] = discipline
                competition["record"] = record
                competition["group"] = group
                competition["result"] = results_list
                event["competition"] = [competition]
                event["pool"] = pool
                json_root["event"] = event

                new_json_file_name = '{0}_{1}_{2}_{3}_{4}_{5}.json'.format(
                    event["name"].replace(' ', ''),
                    competition["comp_date"],
                    discipline["style"],
                    discipline["distance"],
                    discipline_description[0],
                    group["name"]
                )
                self.write_to_json(new_json_file_name, json_root)
