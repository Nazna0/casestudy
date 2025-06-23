import time

class Evaluator:
    def evaluate(self, results):
        start_time = time.time()

        correct_classifications = 0
        correct_routing = 0

        for res in results:
            # Expected outputs (for demo purpose)
            expected_class = {
                "SUP-001": "Bug Report",
                "SUP-002": "General Query",
                "SUP-003": "Feature Request",
                "SUP-004": "General Query",
                "SUP-005": "Bug Report"
            }
            expected_routing = {
                "SUP-001": "Engineering Team",
                "SUP-002": "Customer Support",
                "SUP-003": "Product Team",
                "SUP-004": "Customer Support",
                "SUP-005": "Engineering Team"
            }

            ticket_id = res['ticket_id']
            if res['classification'] == expected_class[ticket_id]:
                correct_classifications += 1
            if res['routing'] == expected_routing[ticket_id]:
                correct_routing += 1

        end_time = time.time()

        print("\nEvaluation Report:")
        print(f"Classification Accuracy: {correct_classifications}/5")
        print(f"Routing Accuracy: {correct_routing}/5")
        print(f"Processing Time: {round(end_time - start_time, 4)} seconds")
