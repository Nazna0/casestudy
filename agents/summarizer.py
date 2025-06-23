class TicketSummarizer:
    def summarize(self, ticket):
        return f"Ticket about '{ticket['subject']}' from {ticket['customer_tier']} tier customer."
