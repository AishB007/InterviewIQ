questions = [ 
    "Tell me about yourself and why you are interested in this role?", 
    "Describe a challenging technical problem you solved.", 
    "Explain a project you worked on and your contribution.",
    "Tell me about a mistake you made and what you learned.", 
    "How would you approach your first 30 days in this role?" 
]

state = { 
    "current": 0, 
    "history": [] 
} 


def get_question(): 
    if state["current"] >= len(questions): 
        return "## Interview Completed\nYou have answered all questions." 
    
    return ( f"### Question {state['current'] + 1} of {len(questions)}\n\n" f"{questions[state['current']]}" )