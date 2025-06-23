# Customer Support Ticket Analyzer & Router

This is a multi-agent AI system built using Python to analyze and route customer support tickets, as part of the Draconic AI Engineer Case Study.

---

## 🚀 Problem Statement

Build a multi-agent system that:
- Classifies support tickets (e.g., Bug Report, Feature Request, General Query)
- Routes the ticket to the correct team (Engineering, Product, Support)
- Summarizes the ticket for quick review

---

## 🧠 Agent Architecture

| Agent | Purpose |
|-------|---------|
| **TicketClassifier** | Determines the type of issue |
| **TicketRouter**     | Routes based on classification & tier |
| **TicketSummarizer** | Provides a short summary |

Each agent is specialized and independent.

---

## 🔍 Sample Input

```json
{
  "ticket_id": "SUP-001",
  "customer_tier": "free",
  "subject": "This product is completely broken!!!",
  "message": "Nothing works! I can't even log in.",
  "previous_tickets": 0,
  "monthly_revenue": 0,
  "account_age_days": 2
}
