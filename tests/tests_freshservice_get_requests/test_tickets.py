from freshservice_get_requests import tickets

class TestAllTickets:

    all_tickets = tickets.all_tickets()

    def test_ticket_type(self):
        assert self.all_tickets