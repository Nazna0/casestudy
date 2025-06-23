from agents.classifier import TicketClassifier
from agents.router import TicketRouter
from agents.summarizer import TicketSummarizer
from evaluation.evaluator import Evaluator
import json

# Sample tickets (from the PDF)
test_tickets = [
    {
        "ticket_id": "SUP-001",
        "customer_tier": "free",
        "subject": "This product is completely broken!!!",
        "message": "Nothing works! I can't even log in. This is the worst software I've ever used.",
        "previous_tickets": 0,
        "monthly_revenue": 0,
        "account_age_days": 2
    },
    {
        "ticket_id": "SUP-002",
        "customer_tier": "enterprise",
        "subject": "Minor UI issue with dashboard",
        "message": "Hi team, just noticed the dashboard numbers are slightly misaligned on mobile view.",
        "previous_tickets": 15,
        "monthly_revenue": 25000,
        "account_age_days": 730
    },
    {
        "ticket_id": "SUP-003",
        "customer_tier": "premium",
        "subject": "Feature Request: Bulk export",
        "message": "We need bulk export functionality for our quarterly reports.",
        "previous_tickets": 5,
        "monthly_revenue": 5000,
        "account_age_days": 400
    },
    {
        "ticket_id": "SUP-004",
        "customer_tier": "premium",
        "subject": "API rate limits unclear",
        "message": "Getting rate limited but documentation says we should have 1000 requests/hour.",
        "previous_tickets": 8,
        "monthly_revenue": 3000,
        "account_age_days": 180
    },
    {
        "ticket_id": "SUP-005",
        "customer_tier": "enterprise",
        "subject": "Urgent: Security vulnerability?",
        "message": "Our security team flagged that your API responses include internal server paths.",
        "previous_tickets": 20,
        "monthly_revenue": 50000,
        "account_age_days": 900
    }
]

classifier = TicketClassifier()
router = TicketRouter()
summarizer = TicketSummarizer()
evaluator = Evaluator()

results = []

for ticket in test_tickets:
    classification = classifier.classify(ticket)
    routing = router.route(ticket, classification)
    summary = summarizer.summarize(ticket)

    results.append({
        'ticket_id': ticket['ticket_id'],
        'classification': classification,
        'routing': routing,
        'summary': summary
    })

# Print Results
for res in results:
    print(json.dumps(res, indent=2))

# Evaluate
evaluator.evaluate(results)
