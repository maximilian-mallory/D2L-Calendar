import re
from ..models import Assignment

def regex_search_in_file(file_path, pattern):
    try:
        assignments = []  # List to hold Assignment objects

        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

            matches = re.findall(pattern, file_content)

            if matches:
                print("Matches found.")
                for match in matches:
                    course = "Environmental Science"
                    date = match[0]  # Assuming match[0] is the date
                    name = match[1]  # Assuming match[1] is the name

                    # Create Assignment instance and add to assignments list
                    assignment = Assignment(course=course, date=date, name=name)
                    
                    assignments.append(assignment)

                Assignment.objects.all().delete() ##!!!!!!Remove after testing
                # Save all Assignment instances to the database
                Assignment.objects.bulk_create(assignments)

            else:
                print("No matches found.")
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
