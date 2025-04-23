import csv
import re

def parse_markdown_to_csv(markdown_path, csv_path):
    with open(markdown_path, 'r') as md_file:
        lines = md_file.readlines()

    phase = None
    current_task = None
    data = []

    for line in lines:
        line = line.strip()

        # Match phase headers
        phase_match = re.match(r"^## (.+)", line)
        if phase_match:
            phase = phase_match.group(1)
            continue

        # Match checklist items
        task_match = re.match(r"^(- \[.\]) (.+)", line)
        if task_match:
            status = 'Done' if task_match.group(1) == '- [x]' else 'Todo'
            task_text = task_match.group(2)

            # Check for subtask (2 spaces or a tab before the dash)
            if line.startswith('  -') or line.startswith('\t-'):
                data.append({
                    'Phase': phase,
                    'Task': task_text,
                    'Parent Task': current_task,
                    'Status': status
                })
            else:
                current_task = task_text  # Update current main task
                data.append({
                    'Phase': phase,
                    'Task': current_task,
                    'Parent Task': '',
                    'Status': status
                })

    # Write to CSV
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['Phase', 'Task', 'Parent Task', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Example usage
parse_markdown_to_csv('ROADMAP.md', 'checklist.csv')
