"""Code-level red-flag triage check. Runs on every turn, on the English translation.

Sources (citable):
- WHO IMCI general danger signs (child): unable to drink/breastfeed, vomits everything,
  convulsions, lethargic or unconscious.
- WHO/ICRC adult emergency signs & Manchester Triage discriminators: chest pain,
  severe respiratory distress, uncontrolled haemorrhage, unresponsiveness, stroke signs,
  seizure, severe dehydration, meningism, poisoning, major trauma.

This is deliberately NOT an LLM call: escalation must be deterministic and testable.
"""
import re

RED_FLAGS = [
    ("chest pain", r"chest\s*(pain|tight|pressure|heaviness)|pain\s+in\s+(my|the)\s+chest"),
    ("breathing difficulty", r"(can'?t|cannot|difficult\w*|trouble|hard)\s+(to\s+)?breath\w*|short(ness)?\s+of\s+breath|gasping"),
    ("uncontrolled bleeding", r"bleed\w*\s+(won'?t|not|doesn'?t)\s+stop|(heavy|uncontrolled|lot of)\s+bleeding"),
    ("unconscious/unresponsive", r"unconscious|unresponsive|fainted|passed\s+out|not\s+waking"),
    ("seizure", r"seizure|convulsion|fits?\b"),
    ("stroke signs", r"face\s+droop\w*|arm\s+weak\w*|slurred\s+speech|one\s+side.*(weak|numb)|sudden.*(numb|weak)"),
    ("severe dehydration (child)", r"(child|baby|infant).*(no\s+urine|sunken|very\s+drowsy|limp)|vomit\w*\s+everything|unable\s+to\s+drink"),
    ("meningism", r"(high\s+)?fever.*(stiff\s+neck|neck\s+stiff)|stiff\s+neck.*fever"),
    ("poisoning/overdose", r"poison\w*|overdose|swallowed\s+(pills|tablets|chemical)"),
    ("severe injury", r"(deep|severe|major)\s+(cut|wound|injury)|bone\s+(sticking|visible)|head\s+injury.*(vomit|unconscious|confus)"),
    ("cardiac pattern", r"(sweat\w*|nausea|left\s+arm|jaw).*(chest|heart)|((chest|heart).*(sweat\w*|nausea|left\s+arm\s+pain))"),
]


def check(english_text: str) -> list[str]:
    """Return list of red-flag labels matched in the text (empty = no escalation)."""
    text = english_text.lower()
    return [label for label, pattern in RED_FLAGS if re.search(pattern, text)]
