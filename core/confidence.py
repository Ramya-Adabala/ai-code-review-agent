def confidence_label(score):

    if score < 50:
        return "VERIFY THIS"

    elif score < 75:
        return "MEDIUM CONFIDENCE"

    else:
        return "HIGH CONFIDENCE"