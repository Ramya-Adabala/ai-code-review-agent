from core.prompts import SYSTEM_PROMPT
import json


def review_code(code):

    """
    Mock AI reviewer for testing/demo purposes
    """

    mock_response = {
        "issues": [
            {
                "type": "style",
                "severity": "low",
                "line": 2,
                "comment": "Consider adding spaces around operators.",
                "confidence": 85
            },
            {
                "type": "performance",
                "severity": "medium",
                "line": 1,
                "comment": "Function may benefit from input validation.",
                "confidence": 72
            }
        ]
    }

    return mock_response