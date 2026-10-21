import re
from collections import Counter


def detect_filler_words(answer: str) -> dict:
    """
    Detect common filler words in a candidate's interview answer.

    Args:
        answer: The candidate's spoken or written answer.

    Returns:
        A dictionary containing detected filler words,
        their counts, total filler count, and total word count.
    """

    filler_words = [
        "um",
        "uh",
        "like",
        "basically",
        "actually",
        "literally",
        "you know",
        "I mean",
        "sort of",
        "kind of",
        "right",
        "so",
    ]

    if not isinstance(answer, str):
        raise TypeError("Answer must be a string.")

    detected = Counter()
    total_words = len(re.findall(r"\b[\w'-]+\b", answer))

    # Match complete phrases or words, ignoring case.
    for filler in filler_words:
        pattern = (
            r"(?<!\w)"
            + re.escape(filler)
            + r"(?!\w)"
        )

        matches = re.findall(pattern, answer, flags=re.IGNORECASE)

        if matches:
            detected[filler] = len(matches)

    total_fillers = sum(detected.values())

    return {
        "detected_filler_words": dict(detected),
        "total_filler_count": total_fillers,
        "total_word_count": total_words,
        "filler_percentage": round(
            (total_fillers / total_words * 100)
            if total_words else 0,
            2,
        ),
    }

def check_star_structure(answer: str) -> dict:
    """
    Check whether an interview answer contains the four STAR components.

    Args:
        answer: The candidate's behavioral interview answer.

    Returns:
        A dictionary containing detected and missing components,
        component status, and a completeness percentage.
    """

    if not isinstance(answer, str):
        raise TypeError("Answer must be a string.")

    # Keywords and phrases commonly associated with each STAR component.
    star_keywords = {
        "situation": [
            "when I",
            "during",
            "while working",
            "at my previous job",
            "in my previous role",
            "the situation",
            "the project",
            "our team was",
            "we were facing",
        ],
        "task": [
            "my responsibility",
            "my role was",
            "I was responsible for",
            "I needed to",
            "I had to",
            "my goal was",
            "the objective was",
            "the task was",
        ],
        "action": [
            "I implemented",
            "I developed",
            "I created",
            "I decided",
            "I analyzed",
            "I improved",
            "I coordinated",
            "I took the initiative",
            "I worked on",
            "I resolved",
        ],
        "result": [
            "as a result",
            "the outcome",
            "the result",
            "this improved",
            "this reduced",
            "this increased",
            "we achieved",
            "I learned",
            "we successfully",
            "saved",
            "increased by",
            "reduced by",
        ],
    }

    text = answer.lower()

    component_status = {}

    for component, keywords in star_keywords.items():
        found = []
        for keyword in keywords:
            if re.search(r"(?<!\w)" + re.escape(keyword) + r"(?!\w)", text, flags=re.IGNORECASE):    
                found.append(keyword)

        # print(f"component {component}: {found}")
        component_status[component] = {
            "present": bool(found),
            "matched_phrases": found,
        }

    present = [
        component
        for component, details in component_status.items()
        if details["present"]
    ]

    missing = [
        component
        for component, details in component_status.items()
        if not details["present"]
    ]

    completeness = round(len(present) / 4 * 100, 2)

    return {
        "star_components": component_status,
        "present_components": present,
        "missing_components": missing,
        "components_present": len(present),
        "total_components": 4,
        "completeness_percentage": completeness,
        "is_complete": len(missing) == 0,
    }

def score_relevance(answer: str, expected_keywords: list[str]) -> dict:
    """
    Calculate answer relevance based on expected keyword coverage.

    Args:
        answer: The candidate's interview answer.
        expected_keywords: Keywords or concepts expected in the answer.

    Returns:
        A dictionary containing the relevance score,
        matched keywords, and missing keywords.
    """

    if not isinstance(answer, str):
        raise TypeError("Answer must be a string.")

    if not isinstance(expected_keywords, list):
        raise TypeError("Expected keywords must be a list.")

    if not expected_keywords:
        return {
            "relevance_score": 0,
            "matched_keywords": [],
            "missing_keywords": [],
            "total_keywords": 0,
            "matched_count": 0,
        }

    text = answer.lower()

    matched_keywords = []
    missing_keywords = []

    for keyword in expected_keywords:

        pattern = (
            r"(?<!\w)"
            + re.escape(keyword.lower())
            + r"(?!\w)"
        )

        if re.search(pattern, text):
            matched_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)

    score = round(
        len(matched_keywords) / len(expected_keywords) * 100
    )

    return {
        "relevance_score": score,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "total_keywords": len(expected_keywords),
        "matched_count": len(matched_keywords),
    }



