import subprocess


print("Add Commit Push")

result = subprocess.run(["git", "status"], capture_output=True, text=True)
# Print the output
print("Executing \"git status\"")
print(result.stdout)
print("STDERR:")
print(result.stderr)

