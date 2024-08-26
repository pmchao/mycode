import subprocess

"""
1: This script retrieves and displays the current Git branch in the repository.
2: version: 1.0
3: Version 2.1
4: Version:3.1
3: version: 2.0
4: version: 3.0

"""

def get_git_branch():
    try:
        # Run the git command to get the current branch
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Check if the command was successful
        if result.returncode == 0:
            print(f"Current Git branch: {result.stdout.strip()}")
        else:
            print("Error: Not a git repository or no branch found.")
    except Exception as e:
        print(f"An error occurred,you are not in git: {e}")

if __name__ == "__main__":
    get_git_branch()
