from git import Repo

def extract_all_file_versions(repo, filepath):
  """
  Extracts all versions of a file from a Git repository and stores them in uniquely named files in chronological order.

  Args:
    repo: A GitPython Repo object representing the Git repository.
    filepath: The path to the file within the repository.
  """
  # Sort commits by commit date in ascending order (oldest first)
  commits = sorted(repo.iter_commits(filepath), key=lambda c: c.committer.date)

  for commit in commits:
    # Get the commit hash
    commit_hash = commit.hexsha

    # Extract the file content
    blob = commit.tree / filepath

    # Create a unique filename with commit hash
    filename = f"{filepath}_{commit_hash}.txt"

    # Write the content to the file
    with open(filename, 'wb') as f:
      f.write(blob.data_stream.read())

    print(f"Extracted version from commit: {commit_hash} - Saved as: {filename}")

# Replace with your Git repository path
repo_path = "/path/to/your/repo"
# Replace with the specific file path within the repo
file_to_extract = "path/to/your/file.txt"

# Open the Git repository
repo = Repo(repo_path)

# Extract all versions of the file in chronological order
extract_all_file_versions(repo, file_to_extract)

