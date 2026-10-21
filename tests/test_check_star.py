from pprint import pprint
from tools import check_star_structure

answer = """
During my second semester, our team was facing a problem with our
college project. I was responsible for improving the application's
performance.

I analyzed the database queries and implemented caching to reduce
unnecessary requests. As a result, the application became faster
and the response time improved.
"""

result = check_star_structure(answer)

pprint(result)
