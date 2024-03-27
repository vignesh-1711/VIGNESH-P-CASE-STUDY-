from dao.crime_analysis_service_impl import CrimeAnalysisServiceImpl
from util.db_conn_util import DBConnUtil
from entity.incident import Incident

def main():
    property_file_name = "database.properties"  # Example property file name
    service = CrimeAnalysisServiceImpl(property_file_name)
    
    # Establish database connection
    connection = DBConnUtil.get_connection()
    if connection:
        try:
            # Example: Create new incident
            new_incident = Incident(incident_id=1, incident_type="Robbery", incident_date="2024-03-28",
                                    location=(40.7128, -74.0060), description="Robbery at downtown",
                                    status="Open", victim_id=101, suspect_id=201)
            success = service.create_incident(new_incident)
            if success:
                print("Incident created successfully.")
            else:
                print("Failed to create incident.")

            # Example: Get list of incidents within a date range
            start_date = "2024-03-01"
            end_date = "2024-03-31"
            incidents = service.get_incidents_in_date_range(start_date, end_date)
            print("Incidents within date range:")
            for incident in incidents:
                print(incident.incident_id, incident.incident_type, incident.incident_date)

            # Example: Update incident status
            incident_id = 1
            new_status = "Closed"
            success = service.update_incident_status(new_status, incident_id)
            if success:
                print(f"Incident status updated successfully for incident ID {incident_id}.")
            else:
                print(f"Failed to update incident status for incident ID {incident_id}.")
        except Exception as e:
            print(f"Error executing operation: {str(e)}")
        finally:
            # Close database connection
            connection.close()
    else:
        print("Failed to establish database connection.")

if __name__ == "__main__":
    main()
