from fastmcp import FastMCP
from tools import (
    get_semester_courses,
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_remaining_credit_hours,
    save_report,
)

mcp = FastMCP("cgpa")

# the docstring and type hints become the description the model reads
mcp.tool(get_semester_courses)
mcp.tool(marks_to_grade_points)
mcp.tool(calculate_semester_gpa)
mcp.tool(calculate_new_cgpa)
mcp.tool(required_gpa_for_target)
mcp.tool(get_remaining_credit_hours)
mcp.tool(save_report)

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)  # http://127.0.0.1:8000/mcp