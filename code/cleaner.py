import re

def clean(text):
    lines = text.split("\n")
    cleaned = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("---"):
            continue
        if "source_url" in line.lower():
            continue
        if "breadcrumbs" in line.lower():
            continue
        if "![" in line:
            continue

        
        line = line.replace("#", "")
        line = line.replace("*", "")
        line = line.replace("\\", "")
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        line = re.sub(r"\s+", " ", line)

        cleaned.append(line)

    result = " ".join(cleaned).strip()
    if len(result) <= 700:
        return result

    sentence_end = max(result.rfind(".", 0, 700), result.rfind("?", 0, 700), result.rfind("!", 0, 700))
    if sentence_end > 250:
        return result[:sentence_end + 1]

    word_end = result.rfind(" ", 0, 700)
    return result[:word_end].strip()
