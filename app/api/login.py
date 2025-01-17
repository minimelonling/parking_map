import json
import os
import pathlib
import sys
sys.path.append(".")

import header

def identify(textContent: header.Info):
    base_path = pathlib.Path().resolve()
    data_path = os.path.join(base_path, "data")

    with open(os.path.join(data_path, "personal_info.json"), "w", encoding="utf8") as f:
        f.write(json.dumps(textContent))
        f.close()

    return None
