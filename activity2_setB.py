
def parse_log_line(log_line):
    # Extract log level (first word before space)
    log_level = log_line.split(" ")[0]
    # Extract message (everything after the timestamp)
    message = log_line.split(" ", 3)[-1]
    return log_level, message

def format_log_summary(log_level, message):
    return "[{}] -> {}".format(log_level, message)


def find_all_emails(text):
    words = text.split()
    emails = [word for word in words if "@" in word and "." in word]
    return emails



def convert_to_title_case(text):
    words = text.split("_")
    title_case = " ".join(word.capitalize() for word in words)
    return title_case


# --------------------------------

print("\n--- Log File Parser ---")

# Task 1: Parse log line
log_line = input("\nEnter a log line (e.g., 'ERROR 2024-10-06 14:35:01 Database connection failed'): ")
log_level, message = parse_log_line(log_line)
print(f"Extracted Log Level: {log_level}")
print(f"Extracted Message: {message}")

# Task 2: Format summary
formatted = format_log_summary(log_level, message)
print(f"\nFormatted Summary:\n{formatted}")

# Task 3: Find all emails
text_input = input("\nEnter a block of text (to find all email addresses): ")
emails = find_all_emails(text_input)
print("Emails found:" if emails else "No emails found.")
for email in emails:
    print("-", email)

# Task 4: Convert to title case
underscore_text = input("\nEnter an underscore_separated_string: ")
title_case_text = convert_to_title_case(underscore_text)
print("Converted to title case:", title_case_text)
