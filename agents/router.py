class TicketRouter:
    def route(self, ticket, classification):
        if classification == "Bug Report":
            return "Engineering Team"
        elif classification == "Feature Request":
            return "Product Team"
        else:  # General Query
            return "Customer Support"
