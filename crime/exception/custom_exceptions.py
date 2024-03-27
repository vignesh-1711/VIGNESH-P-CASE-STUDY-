class IncidentNumberNotFoundException(Exception):
    """Exception raised when an incident number is not found in the database."""
    def __init__(self, message="Incident number not found in database"):
        self.message = message
        super().__init__(self.message)

class CaseNotFoundException(Exception):
    """Exception raised when a case is not found in the database."""
    def __init__(self, message="Case not found in database"):
        self.message = message
        super().__init__(self.message)
