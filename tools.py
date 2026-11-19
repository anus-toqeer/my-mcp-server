import os

COURSES = {
    1: [("MS-251", "Probability & Statistics", 3.0),
        ("GE-160", "Applications of ICT", 3.0),
        ("GE-169", "Applied Physics", 3.0),
        ("GE-167", "Discrete Structures", 3.0),
        ("HQ-001", "Quran Translation - I", 0.5),
        ("GE-190", "Functional English", 3.0)],
    2: [("CC-112", "Programming Fundamentals", 3.0),
        ("CC-112-L", "Programming Fundamentals Lab", 1.0),
        ("CC-110", "Digital Logic Design", 2.0),
        ("CC-110-L", "Digital Logic Design Lab", 1.0),
        ("MS-252", "Linear Algebra", 3.0),
        ("GE-191", "Expository Writing", 3.0),
        ("GE-163", "Islamic Studies", 2.0),
        ("HQ-002", "Quran Translation - II", 0.5)],
    3: [("CC-211", "Object Oriented Programming", 3.0),
        ("CC-211-L", "Object Oriented Programming Lab", 1.0),
        ("CC-215", "Database Systems", 3.0),
        ("CC-215-L", "Database Systems Lab", 1.0),
        ("CC-210", "Computer Organization & Assembly Language", 3.0),
        ("GE-162", "Calculus & Analytical Geometry", 3.0),
        ("GE-192", "Introduction to Management", 2.0),
        ("HQ-003", "Quran Translation - III", 0.5)],
    4: [("CC-213", "Data Structures", 3.0),
        ("CC-213-L", "Data Structures Lab", 1.0),
        ("CC-312", "Information Security", 3.0),
        ("CC-214", "Computer Networks", 3.0),
        ("CC-212", "Software Engineering", 3.0),
        ("DC-220", "Advanced Database Management Systems", 3.0),
        ("HQ-004", "Quran Translation - IV", 0.5)],
    5: [("CC-313", "Analysis of Algorithms", 3.0),
        ("CC-310", "Artificial Intelligence", 3.0),
        ("DC-320", "Theory of Automata and Formal Languages", 3.0),
        ("DC-321", "Human Computer Interaction", 3.0),
        ("DC-322", "Computer Architecture", 3.0),
        ("EC-330", "Web Technologies / Elective", 3.0),
        ("HQ-005", "Quran Translation - V", 0.5)],
    6: [("CC-311", "Operating Systems", 3.0),
        ("EC-333", "Mobile Application Development / Elective", 3.0),
        ("EC-324", "Software Construction & Development / Elective", 3.0),
        ("EC-335", "Machine Learning / Elective", 3.0),
        ("EC-334", "Game Design and Development / Elective", 3.0),
        ("MS-253", "Multivariable Calculus", 3.0),
        ("HQ-006", "Quran Translation - VI", 0.5)],
    7: [("CC-411", "Final Year Project - I", 2.0),
        ("DC-328", "Parallel & Distributed Computing", 3.0),
        ("EC-345", "Computer Vision / Elective", 3.0),
        ("EC-425", "Software Quality Engineering / Elective", 3.0),
        ("MS-254", "Technical and Business Writing", 3.0),
        ("GE-263", "Entrepreneurship", 2.0),
        ("GE-262", "Professional Practices", 2.0),
        ("HQ-007", "Quran Translation - VII", 0.5)],
    8: [("CC-412", "Final Year Project - II", 4.0),
        ("DC-421", "Compiler Construction", 3.0),
        ("UE-272", "Introduction to Marketing", 3.0),
        ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
        ("GE-363", "Civics and Community Engagement", 2.0),
        ("HQ-008", "Quran Translation - VIII", 0.5)],
}

def get_semester_courses(semester: int) -> str:
    """
    Return the list of courses and their credit hours for a given semester
    (1 through 8) in the BS Computer Science scheme of studies.
    Use this when a student asks what courses are in a given semester, or
    when you need the course list to help compute total credit hours.
    """
    if semester not in COURSES:
        return "Error: semester must be between 1 and 8"

    lines = []
    for code, name, credit_hours in COURSES[semester]:
        lines.append(f"{code}: {name} ({credit_hours} credit hours)")

    return "\n".join(lines)


def marks_to_grade_points(marks: int) -> float | str:
    """Convert a student's numeric marks in a single course to a PUCIT grade point (0.0–4.0)."""
    if marks not in range(0,101) :
        return "Error : Invalid Marks Entered"

    elif marks<=100 and marks>=85 :
        return 4.0
    elif marks<85 and marks>=80 :
        return 3.7
    elif marks<80 and marks>=75 :
        return 3.3
    elif marks<75 and marks>=70 :
        return 3.0
    elif marks<70 and marks>=65 :
        return 2.7
    elif marks<65 and marks>60 :
        return 2.3
    elif marks<=60 and marks>=58 :
        return 2.0
    elif marks in range (55,58) :
        return 1.7
    elif marks in range (50,55) :
        return 1.0
    else :
        return 0.0

# print(marks_to_grade_points(58))


def calculate_semester_gpa(grade_points: list[float], credit_hours: list[float]) -> float | str:
    """
    Calculate one semester's credit-weighted GPA.
    Use this once you have the grade points and credit hours for every course
    a student took in a single semester, to compute that semester's overall GPA.
    """
    # Validation: lists must be the same length so each grade point
    # correctly pairs with its matching credit hours
    if len(grade_points) != len(credit_hours):
        return "Error: grade_points and credit_hours must be the same length"

    if len(grade_points) == 0:
        return "Error: no courses provided"

    if any(ch <= 0 for ch in credit_hours):
        return "Error: credit hours must be greater than zero"

    # zip() pairs up corresponding elements from both lists,
    # index by index: (grade_points[0], credit_hours[0]), (grade_points[1], credit_hours[1]), ...
    numerator = sum(gp * ch for gp, ch in zip(grade_points, credit_hours))

    # numerator = 0
    # for gp, ch in zip(grade_points, credit_hours):
    #    numerator += gp * ch

    denominator = sum(credit_hours)

    gpa = numerator / denominator
    return round(gpa, 2)

# print(calculate_semester_gpa([4.0, 3.3, 2.7], [3.0, 3.0, 1.0])) 


def calculate_new_cgpa(current_cgpa: float, completed_credit_hours: float,
                        semester_gpa: float, semester_credit_hours: float) -> float | str:
    """
    Project a student's new overall CGPA after completing one more semester.
    Use this when you know a student's current CGPA and completed credit hours,
    plus their GPA and credit hours for a semester just finished (or hypothetically
    planned), to compute the resulting overall CGPA.
    """
    # CGPA/GPA on this scale can't exceed 4.0 or go below 0.0
    if not (0.0 <= current_cgpa <= 4.0):
        return "Error: current_cgpa must be between 0.0 and 4.0"

    if not (0.0 <= semester_gpa <= 4.0):
        return "Error: semester_gpa must be between 0.0 and 4.0"

    if completed_credit_hours < 0:
        return "Error: completed_credit_hours cannot be negative"

    if semester_credit_hours <= 0:
        return "Error: semester_credit_hours must be greater than zero"

    numerator = (current_cgpa * completed_credit_hours) + (semester_gpa * semester_credit_hours)
    denominator = completed_credit_hours + semester_credit_hours

    new_cgpa = numerator / denominator
    return round(new_cgpa, 2)

# print(calculate_new_cgpa(3.6,49,4,17))

def required_gpa_for_target(target_cgpa: float, current_cgpa: float, completed_credit_hours: float, remaining_credit_hours: float) -> float | str:
    """
    Calculate the GPA a student needs to earn on their remaining credit hours
    to reach a target CGPA by graduation (or by any future point).
    Use this whenever a student states a CGPA goal and asks what GPA they need
    from here. Note: the result can exceed 4.0, meaning the target is not
    reachable in the given number of remaining credit hours — the caller
    (agent) is responsible for widening the horizon and trying again, not
    this tool.
    """
    if not (0.0 <= target_cgpa <= 4.0):
        return "Error: target_cgpa must be between 0.0 and 4.0"

    if not (0.0 <= current_cgpa <= 4.0):
        return "Error: current_cgpa must be between 0.0 and 4.0"

    if completed_credit_hours < 0:
        return "Error: completed_credit_hours cannot be negative"

    if remaining_credit_hours <= 0:
        return "Error: remaining_credit_hours must be greater than zero"

    total_hours_at_end = completed_credit_hours + remaining_credit_hours
    numerator = (target_cgpa * total_hours_at_end) - (current_cgpa * completed_credit_hours)

    required_gpa = numerator / remaining_credit_hours
    return round(required_gpa, 2)

# print(required_gpa_for_target(3.75,3.7,66,17))


def get_remaining_credit_hours(current_semester: int) -> float | str:
    """
    Total the credit hours of all semesters that come AFTER the given
    (completed) semester, based on the official scheme of studies.
    Use this when a student tells you the last semester they've completed
    and you need to know how many credit hours are left until graduation
    (semester 8). For example, current_semester=4 sums semesters 5-8.
    """
    if current_semester not in COURSES:
        return "Error: current_semester must be between 1 and 8"

    total = 0.0
    for semester_number, courses in COURSES.items():
        if semester_number > current_semester:
            for code, name, credit_hours in courses:
                total += credit_hours

    return round(total, 2)


def save_report(filename: str, content: str) -> str:
    """
    Save a summary report (e.g. a semester GPA result, a projected CGPA, or a
    plan for reaching a target CGPA) to a text file on disk.
    Use this ONLY when the student explicitly asks you to save something,
    and only after you've already produced a real result worth keeping —
    never after just a clarifying question.
    """
    if not filename.strip():
        return "Error: filename cannot be empty"

    if not content.strip():
        return "Error: content cannot be empty"

    # make sure it always has a .txt extension, so the file is readable/predictable
    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        with open(filename, "w") as f:
            f.write(content)
        return f"Report saved successfully as {filename}"
    except Exception as e:
        return f"Error: could not save file - {str(e)}"