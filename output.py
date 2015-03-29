import git
import os
import shutil
import tempfile

__author__ = 'MrPatiwi'


class Student:

    def __init__(self, name, username, section):
        self.name = name
        self.username = username
        self.section = section

    @classmethod
    def from_data(cls, line_data):
        data = line_data.split('\t')
        return cls(name=' '.join(data[2:5]), section=data[0], username=data[-1])

    @classmethod
    def load_from_file(cls, file="students.txt"):
        with open(file, "rt", encoding='utf16') as f:
            return [cls.from_data(line_data.strip()) for line_data in f]

    def __str__(self):
        return "(Sec. {}) {}: {}".format(self.section, self.name, self.username)


class GitWrap:

    @classmethod
    def repo(cls, dir):
        return git.Repo(path=dir)

    @classmethod
    def clone(cls, dir, url):
        return git.Repo.clone_from(url, dir)

    @classmethod
    def pull(cls, dir):
        repo = cls.repo(dir)
        origin = repo.remotes.origin
        return origin.pull()


    @classmethod
    def copy_file(cls, from_path, to_path):
        return shutil.copy2(from_path, to_path)

    @classmethod
    def copy_dir(cls, from_path, to_path):
        return shutil.copytree(from_path, to_path)


    @classmethod
    def commit(cls, dir, message):
        repo = cls.repo(dir)
        repo.git.add(all=True)
        repo.git.commit(message=message)
        origin = repo.remotes.origin
        return origin.push()


    @classmethod
    def __execute(cls, command, *args):
        from subprocess import call, PIPE
        return call(command, *args, shell=True)  #, stdout=PIPE)

    # @classmethod
    # def pull(cls):
    #     return cls.__execute("git pull")

    @classmethod
    def add(cls, *args):
        return cls.__execute("git add", *args)

if __name__ == '__main__':
    for student in Student.load_from_file():
        print(student)

    print(GitWrap.pull("/Users/MrPatiwi/repos/Realm-JSON"))
