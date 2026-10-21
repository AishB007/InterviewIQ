
from pprint import pprint

from tools import score_relevance


question_keywords = [
    "Python",
    "SQL",
    "data analysis",
    "database",
    "application",
]

candidate_answer = """
I built a data analysis application using Python and SQL.
I connected the application to a database to retrieve records.
"""

result = score_relevance(
    answer=candidate_answer,
    expected_keywords=question_keywords,
)

pprint(result)
