
def cleanup_title (title):
    title = title.replace('/', '_')
    title = title.replace("\r", "")
    title = title.replace("\n", "")
    title = title.replace("®", "")
    title = title.replace("™", "")
    title = title.replace(":", " - ")
    while "  " in title:
        title = title.replace("  ", " ")
    return title
