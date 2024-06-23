#feedback1.txt
'''
Kartik: 5 - Great Service!
# Harsh: 2 - Not satisfied.
'''
#feedback2.txt
'''
Aditya: 4 - Good, but could improve.
Sankalp: 3 - Average experience.
'''
#feedback3.txt
'''
Roshan: 5 - Excellent!
Lakshit: 1 - Very poor service.
'''
def read_feedback_files(file_names):

    feedback_data = []
    for file_name in file_names:
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    try:
                        customer_name, rest = line.strip().split(': ', 1)
                        rating, comment = rest.split(' - ', 1)
                        rating = int(rating)
                        feedback_data.append({
                            'customer_name': customer_name,
                            'rating': rating,
                            'comment': comment
                        })
                    except ValueError:
                        print(f"Line in file '{file_name}' is malformed: {line.strip()}")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred while reading '{file_name}': {e}")
    return feedback_data

def process_feedback_data(feedback_data):

    if not feedback_data:
        print("No feedback data found.")
        return None
    
    total_ratings = sum(feedback['rating'] for feedback in feedback_data)
    average_rating = total_ratings / len(feedback_data)
    return average_rating

def write_summary_file(feedback_data, average_rating):

    with open('feedback_summary.txt', 'w') as file:
        file.write(f"Total Feedback Entries: {len(feedback_data)}\n")
        if average_rating is not None:
            file.write(f"Average Rating: {average_rating:.2f}\n")
        else:
            file.write("Average Rating: N/A\n")
        file.write("\nFeedbacks:\n")
        for feedback in feedback_data:
            file.write(f"{feedback['customer_name']}: {feedback['rating']} - {feedback['comment']}\n")

file_names = ['feedback1.txt', 'feedback2.txt', 'feedback3.txt']
feedback_data = read_feedback_files(file_names)
average_rating = process_feedback_data(feedback_data)
write_summary_file(feedback_data, average_rating)

# Total Feedback Entries: 6
# Average Rating: 3.33

# Feedbacks:
# Kartik: 5 - Great Service!
# Harsh: 2 - Not satisfied.
# Aditya: 4 - Good, but could improve.
# Sankalp: 3 - Average experience.
# Roshan: 5 - Excellent!
# Lakshit: 1 - Very poor service.
