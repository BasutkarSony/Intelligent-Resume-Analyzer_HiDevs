from report import generate_report
from matcher import match_candidate
import json
# Read resume file

resume_file = input("Enter resume filename: ")

try:
    with open(f"resumes/{resume_file}", "r") as file:
        resume_text = file.read()

except FileNotFoundError:
    print("Resume file not found.")
    exit()

# Split text into lines
lines = resume_text.split("\n")

# Variables
name = ""
email = ""
skills = []
experience = 0

# Extract data
for line in lines:

    if line.startswith("Name:"):
        name = line.replace("Name:", "").strip()

    elif line.startswith("Email:"):
        email = line.replace("Email:", "").strip()

    elif line.startswith("Skills:"):
        skill_text = line.replace("Skills:", "").strip()

        # Convert skills into list
        skills = skill_text.split(",")

        # Remove extra spaces
        skills = [skill.strip() for skill in skills]

    elif line.startswith("Experience:"):
        experience = int(
            line.replace("Experience:", "")
            .replace("years", "")
            .strip()
        )

# Print extracted details
print("Candidate Name:", name)
print("Candidate Email:", email)
print("Candidate Skills:", skills)
print("Candidate Experience:", experience)

# Store candidate data in dictionary

candidate = {
    "name": name,
    "email": email,
    "skills": skills,
    "experience": experience
}

# Print dictionary
print("\nCandidate Profile:")
print(candidate)

# Save candidate profile to JSON file

with open("output/candidate.json", "w") as json_file:
    json.dump(candidate, json_file, indent=4)

print("\nCandidate profile saved to output/candidate.json")

# Load candidate profile from JSON file

with open("output/candidate.json", "r") as json_file:
    loaded_candidate = json.load(json_file)

print("\nLoaded Candidate Profile:")
print(loaded_candidate)

matched_skills, missing_skills, match_score = match_candidate(
    loaded_candidate["skills"]
)

# Print results
print("\nJob Match Analysis")
print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)
print("Match Score:", round(match_score, 2))

# Generate final report

final_report = generate_report(
    loaded_candidate,
    matched_skills,
    missing_skills,
    match_score
)

# Print final report
print(final_report)

# Save report to text file

with open("output/report.txt", "w") as report_file:
    report_file.write(final_report)

print("Report saved to output/report.txt")