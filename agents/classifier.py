class TicketClassifier:
    def classify(self, ticket):
        subject = ticket['subject'].lower()
        message = ticket['message'].lower()
        # High confidence bug words
        if any(word in subject or word in message for word in ["error", "broken", "fail", "vulnerability", "bug", "security"]):
            return "Bug Report"
        # Feature Request
        elif "feature" in subject or "feature" in message:
            return "Feature Request"
        # 'issue' word alone is too vague — treat as General Query unless stronger bug words exist
        else:
            return "General Query"
