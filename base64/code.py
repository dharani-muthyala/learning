import base64
import os
import mimetypes

def file_to_base64(file_path, output_file=None):
    with open(file_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode("utf-8")
        extension = os.path.splitext(file_path)[1].lower()
        if extension == ".pdf":
            mime_type = "application/pdf"
        elif extension == ".xml":
             mime_type = "text/xml"
        else:
             mime_type = "application/octet-stream"

    encoded = f"data:{mime_type};base64,{encoded}"
    
    if output_file:
        with open(output_file, "a") as out:   # Append mode
            out.write(f"\n\n----- {os.path.basename(file_path)} -----\n")
            out.write(encoded)
            out.write("\n")

    return encoded


if __name__ == "__main__":
    file_path = input("Enter the file path: ").strip()

    if not os.path.exists(file_path):
        print("File not found!")
    else:
        base64_data = file_to_base64(file_path, "base64_output.txt")
        print("Conversion successful!")
        print(f"Base64 length: {len(base64_data)} characters")
        print("Saved to: base64_output.txt")