import subprocess

"""
This script retrieves and displays the current Git branch in the repository.
It uses the subprocess module to run the Git command `git rev-parse --abbrev-ref HEAD`.
If the script is run within a Git repository, it will print the name of the current branch.
If it's not run within a Git repository, or if any error occurs, it will display an error message.
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
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_git_branch()
