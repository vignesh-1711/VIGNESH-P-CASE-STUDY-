from abc import ABC, abstractmethod
from entity.incident import Incident

class ICrimeAnalysisService(ABC):
    @abstractmethod
    def create_incident(self, incident: Incident) -> bool:
        pass

    @abstractmethod
    def update_incident_status(self, status: str, incident_id: int) -> bool:
        pass

    @abstractmethod
    def get_incidents_in_date_range(self, start_date: str, end_date: str) -> list:
        pass

    @abstractmethod
    def search_incidents(self, criteria: str) -> list:
        pass

    @abstractmethod
    def generate_incident_report(self, incident: Incident):
        pass

    @abstractmethod
    def create_case(self, case_description: str, incidents: list):
        pass

    @abstractmethod
    def get_case_details(self, case_id: int):
        pass

    @abstractmethod
    def update_case_details(self, case):
        pass

    @abstractmethod
    def get_all_cases(self) -> list:
        pass
