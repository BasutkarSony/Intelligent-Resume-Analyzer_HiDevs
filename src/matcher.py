# Job requirements
required_skills = ["Python", "SQL", "Docker"]


def match_candidate(candidate_skills):

    # Find matched skills
    matched_skills = []

    for skill in required_skills:
        if skill in candidate_skills:
            matched_skills.append(skill)

    # Find missing skills
    missing_skills = []

    for skill in required_skills:
        if skill not in candidate_skills:
            missing_skills.append(skill)

    # Calculate score
    match_score = (
        len(matched_skills) / len(required_skills)
    ) * 100

    return matched_skills, missing_skills, match_score