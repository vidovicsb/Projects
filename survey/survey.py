class AnonymousSurvey:
    """Collect anoymous answers to a survey question."""
    
    def __init__(self, question):
        """Store a question, and prepare to store answers"""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """Show the question"""
        print(self.question)
        
    def store_response(self, new_response):
        """Stores a single response to the question"""
        self.responses.append(new_response)
        
    def show_results(self):
        """Prints out the responses"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
            

