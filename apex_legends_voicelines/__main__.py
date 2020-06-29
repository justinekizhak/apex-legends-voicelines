import random
import json
from typing import List, Dict, Optional
import importlib.resources as pkg_resources
from apex_legends_voicelines import assets

"""Legends:
1. mirage
2. wraith
3. lifeline
4. bangalore
5. octane
6. wattson
7. loba
8. revenant
9. crypto
10. pathfinder
11. gibralter
12. caustic
13. bloodhound
"""


def read_json_from_file(file_name: str):
    data = pkg_resources.read_text(assets, file_name)
    res = json.loads(data)
    return res


def main():
    legends = read_json_from_file("voicelines.json")
    voice_lines = create_voice_lines(legends)
    quote = random.choice(voice_lines)
    print(quote, end="")


def create_voice_lines(
    legends: Dict, whitelist: Optional[List[str]] = None,
) -> List[str]:
    voice_lines = []
    for legend_name, legend in legends.items():
        if check_name_in_list(legend_name, whitelist):
            for key, value in legend.items():
                if key != "name":
                    voice_lines += append_name_to_lines(value, legend["name"])
    return voice_lines


def append_name_to_lines(input_list: List[str], name: str) -> List[str]:
    data = []
    for i in input_list:
        data.append(i + " - " + name)
    return data


def check_name_in_list(name: str, whitelist: Optional[List[str]] = []) -> bool:
    """Check if the name is in the whitelist
    """
    if whitelist is None:
        return True
    if name in whitelist:
        return True
    return False


if __name__ == "__main__":
    main()
