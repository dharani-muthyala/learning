"""import base64

# Read the Base64 string
with open("base64_output.txt", "r") as file:
    base64_string = file.read()

# Decode and save as a new PDF
pdf_bytes = base64.b64decode(base64_string)

with open("decoded.pdf", "wb") as file:
    file.write(pdf_bytes)

print("Decoded PDF created successfully.")"""


import base64
import re

with open("base64_output.txt", "r") as file:
    content = file.read()

# Match each section:
# ----- filename -----
# base64 content
pattern = r"-----\s*(.*?)\s*-----\s*([\s\S]*?)(?=\n-----|\Z)"

matches = re.findall(pattern, content)

# which file to decode
target_file = input("Enter the file name to decode : ").strip()

for filename, base64_data in matches:
    # Skip all other files
    if filename != target_file:
        continue
    base64_data = base64_data.strip()

    if not base64_data:
        continue

    if "," in base64_data:
       base64_data = base64_data.split(",", 1)[1]

    decoded_bytes = base64.b64decode(base64_data)

    with open(filename, "wb") as output_file:
        output_file.write(decoded_bytes)

    print(f"Decoded: {filename}")    
    break
else:
    print("File not found in base64_output.txt")
