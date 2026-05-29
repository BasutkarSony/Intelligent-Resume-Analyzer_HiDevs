def generate_report(candidate,
                    matched_skills,
                    missing_skills,
                    match_score):
    if match_score >= 80:
        recommendation = "Strongly Recommended"
    elif match_score >= 60:
        recommendation = "Recommended"
    else:
        recommendation = "Not Recommended"

    report = f"""
========== RESUME ANALYSIS REPORT ==========

Candidate Name: {candidate['name']}
Candidate Email: {candidate['email']}

Skills: {candidate['skills']}
Experience: {candidate['experience']} years

Matched Skills: {matched_skills}
Missing Skills: {missing_skills}

Match Score: {round(match_score, 2)}%
Recommendation: {recommendation}

============================================
"""

    return report