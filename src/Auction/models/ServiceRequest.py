class ServiceRequest:
    def __init__(self, srid, client_id, service_type, status):
        self.srid = srid
        self.client_id = client_id
        self.service_type = service_type
        self.status = status

    def request_service(self):
        print(f"Service Request ID: {self.srid} for Client ID {self.client_id} has been submitted.")

    def approve_service_request(self):
        self.status = 'approved'
        print(f"Service Request ID: {self.srid} has been approved.")

    def __str__(self):
        return f"Service Request ID: {self.srid}, Client ID: {self.client_id}, Service Type: {self.service_type}, Status: {self.status}"
