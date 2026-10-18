class File:

    def __init__(self,
                 name: str = "",
                 extension: str = "",
                 size: int = ""):
        self.name = name
        self.extension = extension
        self.size = size

    def __str__(self):
        return f"{self.name}.{self.extension} ({self.size} KB)"
    
class Folder:

    def __init__(self,
                 name: str = "folder"):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)

    def print_tree(self, level = 0):
        print("\t" * level, f"{self.name}/")
        level += 1
        for item in self.children:
            if isinstance(item, Folder):
                item.print_tree(level=level)
            elif isinstance(item, File):
                print("\t" * level, f"{item}")

    def get_longest_path(self):
        if not self.children:
            return self.name

        paths = []
        for item in self.children:
            if isinstance(item, Folder):
                paths.append(item.get_longest_path())
            elif isinstance(item, File):
                paths.append(str(item))

        longest_child = max(paths, key=len)

        return f"{self.name}/{longest_child}"

def main():
    root = Folder("root")
    docs = Folder("documents")
    media = Folder("media")
    work_projects = Folder("work_projects")
    archive_2026 = Folder("archive_2026")
    empty_dir = Folder("empty_folder")

    readme = File("readme", "md", 12)
    resume = File("file", "pdf", 450)
    song = File("video", "mp3", 8400)
    secret_report = File("excel_table", "xlsx", 2048)

    
    archive_2026.add(secret_report)
    work_projects.add(archive_2026)

    docs.add(resume)
    docs.add(work_projects)
    media.add(song)

    root.add(readme)
    root.add(docs)
    root.add(media)
    root.add(empty_dir)

    root.print_tree()

    longest_path = root.get_longest_path()
    print(f"\nНайдовший шлях: \n{longest_path}")

if __name__ == "__main__":
    main()
