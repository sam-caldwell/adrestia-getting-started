"""
    (c) 2018-2019 Sam Caldwell.  All Rights Reserved.
"""
import sys
import shutil
from os import path
from os.path import dirname, exists
from subprocess import run
import setuptools.command.build_py

HERE = path.abspath(dirname(dirname(dirname(__file__))))
SETUP_DIR = path.join(HERE, 'setup')


class InitializeProject(setuptools.command.build_py.build_py):
    """
        Clean artifacts (*.egg-info and build/)
    """

    @staticmethod
    def write_file(name: str, prompt: str) -> dict:
        """

        :param name:
        :param prompt:
        :return: dict
        """
        with open(path.join(SETUP_DIR, name + ".txt"), 'w') as file_handle:
            data = input(prompt + ": ")
            file_handle.write(data)
            return data

    @staticmethod
    def generate_readme(data: dict):
        """

        :param data:
        :return:
        """
        readme_file = "README.md"
        with open(path.join(HERE, readme_file), 'w') as file_handle:
            file_handle.write(
                f"# {data['PROJECT_NAME']}\n"
                "=========================================================\n\n"
                f"{data['COPYRIGHT']}\n\n"
                "## Author\n"
                f"{data['AUTHOR']} <{data['AUTHOR_EMAIL']}>\n\n"
                "## Source Repo:\n"
                f"`{data['SOURCE_REPO']}`\n\n"
                "## Description\n"
                f"{data['DESCRIPTION']}\n\n"
                "## Getting Started\n"
                "<content needed>\n\n"
            )

    @staticmethod
    def setup_repo(source_repo: str) -> str:
        """

        :param source_repo:
        :return:
        """

        def sanitize(repo_url: str) -> str:
            """

            :param repo_url:
            :return:
            """
            banned_chars = [';', '`', '&', '|', '"', '<', '>', '#', '%',
                            '{', '}', '\\', '^', '~', '[', ']']

            try:
                assert repo_url[0:4] != "file", "file:// url scheme is banned."
                assert repo_url[0:5] != "http:", "http:// is insecure."
                assert repo_url[0:4] == "git@" \
                    or repo_url[0:5] == "https" \
                    or repo_url[0:3] == "ssh", \
                    "We expect git@, https or ssh"
                for c in banned_chars:
                    assert repo_url.find(c) == -1, \
                        f"'{c}' character found in url"
                return repo_url
            except AssertionError as error:
                print("A bad source code repo was detected.\n"
                      f"repo:{repo_url}\nerror:{error}")
                sys.exit(99)

        git_dir = path.join(HERE, '.git')
        try:
            if exists(git_dir):
                shutil.rmtree(git_dir)
        except Exception as error:
            print("Error initializing project.  "
                  "Could not remove existing .git directory."
                  f"Exception: {error}")
            sys.exit(1)
        try:
            result = run(["git", "init"], shell=False)
            assert result.returncode == 0, "Error calling git init."
            result = run(
                ["git", "remote", "add", "origin", sanitize(source_repo)],
                shell=False)
            assert result.returncode == 0, "Error adding source_repo."
            result = run(["git", "remote", "-v"], shell=False)
            assert result.returncode == 0, "Error listing remote repos."
            print(result.stdout)
        except Exception as error:
            print("Error initializing project.  "
                  "Could not create git repo."
                  f"Exception: {error}")
            sys.exit(1)

    def run(self):
        """
            On build, bump the version.
            :return:
        """
        if exists(path.join(SETUP_DIR, "INITIALIZED.txt")):
            print("You cannot initialize a project twice.  "
                  "If you'd like to use this tool, please delete the file "
                  "setup/INITIALIZED.txt and re-run this command.")
            sys.exit(1)
        else:
            self.generate_readme(data={
                "PROJECT_NAME": self.write_file(
                    'PROJECT_NAME', "Project Name"
                ),
                "AUTHOR": self.write_file(
                    'AUTHOR', "Author"
                ),
                "AUTHOR_EMAIL": self.write_file(
                    'AUTHOR_EMAIL', "Author's email"
                ),
                "COPYRIGHT": self.write_file(
                    'COPYRIGHT', "Copyright notice"
                ),
                "DESCRIPTION": self.write_file(
                    'DESCRIPTION', "Describe the project"
                ),
                "URL": self.write_file(
                    'URL', "Project url"
                ),
                "SOURCE_REPO": self.setup_repo(
                    self.write_file(
                        "SOURCE_REPO",
                        "Code Repository: ",
                    )
                ),
            })
            with open(path.join(SETUP_DIR, "INITIALIZED.txt"), 'w') as tgt:
                tgt.write("")
            print("Your project is initialized.  Your options have been saved "
                  "in the setup/ directory as .txt files and will be "
                  "automatically used by setup.py."
                  ""
                  "Please remember to add content to CLASSIFIERS.txt before"
                  "pushing to pypi.  The following classifiers are set by"
                  "default:\n")
            print("For more information, see https://pypi.org/classifiers/\n")
            with open(path.join(SETUP_DIR, "CLASSIFIERS.txt"), 'r') as src:
                print(src.read())
            print("\nHappy Hacking.")
