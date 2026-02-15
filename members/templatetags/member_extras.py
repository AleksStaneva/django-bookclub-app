from django import template

register = template.Library()


@register.filter
def highlight_score(score):
    if score >= 50:
        return f"{score} *"
    return score
