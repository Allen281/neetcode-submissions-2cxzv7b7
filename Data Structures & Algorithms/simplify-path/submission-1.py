class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.split(r'/+', path)
        folders = []

        for name in path:
            if not name or name == '.':
                continue

            if name == '..':
                if folders:
                    folders.pop()
            else:
                folders.append(name)
        
        return '/' + '/'.join(folders)