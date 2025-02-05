from pathlib import Path

path = Path("programming.txt")

message = "1"

for i in range(2, 101):
    message += f"\n{i}"

print(message)

path.write_text(message)