import re

class Scanner:
    regexList = []

    def addCmd(self, regex, id):
        self.regexList.append((regex, id))

    # return only FIRST match
    def scan(self, text):
        for (regex, id) in self.regexList:
            if re.match(regex, text, re.DOTALL+re.MULTILINE):
                return id
        return None