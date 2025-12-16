from dataclasses import dataclass
from typing import Optional, List

MOVE_VERBS={"go","move","walk"}
NORTH_WORDS={"n","north","up"}
EAST_WORDS={"e","east","right"}
SOUTH_WORDS={"s","south","down"}
WEST_WORDS={"w","west","left"}

DIRECTION_WORDS=NORTH_WORDS|EAST_WORDS|SOUTH_WORDS|WEST_WORDS


DIR_NORMLIZE={}
for w in NORTH_WORDS:
DIR_NORMILIZE[w]="north"
for w in EAST_WORDS:
DIR_NORMILIZE[w]="east"
for w in SOUTH_WORDS:
DIR_NORMILIZE[w]="south"
for w in WEST_WORDS:
DIR_NORMILIZE[w]="west"

DIR_ORDER=["north","east","south","west"]
DIR_INDEX={d:i for i,d in enumerate(DIR_ORDER)}

@dataclass
class Command:
    verb: str
    obj: Optional[str] = None
    target: Optional[str] = None
    raw: str = ""

def parse_command(user_input: str) -> Optional[Command]:
    text = user_input.strip().lower()
    if not text:
        return None

    parts = text.split()

    if len(parts) == 1 and parts[0] in DIRECTION_SYNONYMS:
        return Command(verb="go", target=DIRECTION_SYNONYMS[parts[0]], raw=user_input)

    verb = VERB_SYNONYMS.get(parts[0])
    if not verb:
        return Command(verb="unknown", raw=user_input)

    if verb == "go":
        if len(parts) > 1 and parts[1] in DIRECTION_SYNONYMS:
            return Command(verb="go", target=DIRECTION_SYNONYMS[parts[1]], raw=user_input)
        return Command(verb="go", raw=user_input)

    if verb in ["look", "take", "drop", "use", "unlock"]:
        obj = " ".join(parts[1:]) if len(parts) > 1 else None
        return Command(verb=verb, obj=obj, raw=user_input)

    return Command(verb=verb, raw=user_input)
