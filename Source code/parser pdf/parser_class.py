from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def get_stages(self):
        pass

    @abstractmethod
    def get_competitions(self):
        pass

    @abstractmethod
    def get_athlete_groups(self):
        pass

    @abstractmethod
    def get_results(self):
        pass

    @abstractmethod
    def get_record_row(self):
        pass

    @abstractmethod
    def get_competition_city(self):
        pass

    @abstractmethod
    def get_competition_date(self):
        pass

    @abstractmethod
    def get_event_name(self):
        pass

    @abstractmethod
    def get_headers(self):
        pass

    @abstractmethod
    def get_pool(self):
        pass

    @abstractmethod
    def read_data_from_file(self):
        pass

    @abstractmethod
    def write_to_json(self):
        pass




