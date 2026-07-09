import ollama
import time

print("=" * 70)
print("        Enterprise AI Operations Assistant")
print("      Big Data + AI Incident Investigation")
print("=" * 70)

print("\nLoading AI Model...")
time.sleep(1)

print("Connecting to Enterprise Log Repository...")
time.sleep(1)

print("Reading Production Logs...")
time.sleep(1)

# Read last 200 logs for faster response
with open("logs.txt", "r") as f:
    logs = "".join(f.readlines()[-200:])

print(f"\nLoaded {len(logs.splitlines())} production log entries.")

while True:

    print("\n" + "=" * 70)
    print("1. Incident Summary")
    print("2. Root Cause Analysis")
    print("3. Top Failed APIs")
    print("4. Generate Stakeholder Email")
    print("5. Business Impact")
    print("6. Ask Your Own Question")
    print("7. Exit")
    print("=" * 70)

    choice = input("Enter Choice : ")

    if choice == "1":

        question = """
Summarize today's production incident.

Include:
1. Overall Summary
2. Critical Issues
3. Recommendations

Use proper headings.
"""

    elif choice == "2":

        question = """
Analyze the production logs.

Identify:
1. Root Cause
2. Failed Services
3. Most Frequent Errors
4. Engineering Recommendations

Use headings.
"""

    elif choice == "3":

        question = """
Analyze these logs and identify:

1. Top Failed APIs
2. Top Error Messages
3. Top Warning Messages

Present the results in bullet points.
"""

    elif choice == "4":

        question = """
Generate a professional email to stakeholders.

Include:

Subject

Incident Summary

Business Impact

Recommended Next Steps

Keep it professional.
"""

    elif choice == "5":

        question = """
Explain the business impact.

Include:

Customer Impact

Operational Impact

Business Risk

Future Recommendations
"""

    elif choice == "6":

        question = input("\nAsk Your Question : ")

    elif choice == "7":

        print("\nThank you for using Enterprise AI Operations Assistant.")
        break

    else:

        print("Invalid Choice")
        continue

    prompt = f"""
You are an Enterprise Production Support AI Assistant.

You are helping:

- Developers
- QA Engineers
- DevOps Engineers
- Site Reliability Engineers
- Delivery Managers

You are analyzing enterprise production logs.

Your responsibilities are:

- Detect recurring issues
- Identify root causes
- Explain business impact
- Suggest engineering recommendations

Only answer using information available in the logs.

Production Logs

{logs}

User Request

{question}
"""

    print("\nAI is analyzing production logs...\n")

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("\n" + "=" * 70)
    print(response["message"]["content"])
    print("=" * 70)