from freshservice_get_requests import tickets

class TestAllTickets:

    all_tickets = tickets.all_tickets()

    def test_ticket_type(self):
        assert self.all_tickets

    def test_ticket_is_dict(self):
        """The all_tickets function should be a dict
        """
        assert isinstance(self.all_tickets, dict)

    def test_list_in_dict(self):
        """The all_tickets function should be a dict with a list inside of it.
        """
        list_of_tickets = self.all_tickets["tickets"]
        assert isinstance(list_of_tickets, list)

    def test_dict_data(self):
        for single_ticket in self.all_tickets["tickets"]:
            assert isinstance(single_ticket["cc_emails"], list)

            assert isinstance(single_ticket["fwd_emails"], list)

            assert isinstance(single_ticket["reply_cc_emails"], list)

            assert isinstance(single_ticket["fr_escalated"], bool)

            assert isinstance(single_ticket["spam"], bool)

            assert not single_ticket["email_config_id"]

            group_id = single_ticket["group_id"]
            assert not group_id or isinstance(group_id, int)

            assert isinstance(single_ticket["priority"], int)

            assert isinstance(single_ticket["requester_id"], int)

            responder_id = single_ticket["responder_id"]
            assert not responder_id or isinstance(responder_id, int)

            assert isinstance(single_ticket["source"], int)

            assert isinstance(single_ticket["status"], int)

            assert isinstance(single_ticket["subject"], str)

            assert not single_ticket["to_emails"]

            assert isinstance(single_ticket["department_id"], int)

            assert isinstance(single_ticket["id"], int)

            assert isinstance(single_ticket["type"], str)

            assert isinstance(single_ticket["due_by"], str)

            assert isinstance(single_ticket["fr_due_by"], str)

            assert isinstance(single_ticket["is_escalated"], bool)

            assert isinstance(single_ticket["description"], str)

            assert isinstance(single_ticket["description_text"], str)

            category = single_ticket["category"]
            assert not category or isinstance(category, str)

            sub_category = single_ticket["sub_category"]
            assert not sub_category or isinstance(sub_category, str)

            item_category = single_ticket["item_category"]
            assert not item_category or isinstance(item_category, str)

            assert isinstance(single_ticket["custom_fields"], dict)

            assert isinstance(single_ticket["created_at"], str)

            assert isinstance(single_ticket["updated_at"], str)

            assert isinstance(single_ticket["deleted"], bool)



