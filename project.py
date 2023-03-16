from pdf import PDF
from quiz import Quiz, MCQ, Essay
import inflect

def main():
    print("\tWELCOME TO THE QUIZ GENERATOR, A CS50P FINAL PROJECT\n")
    file_name = input(">>> Enter file name... ")

    # Populating the dictionary, then passing it to fpdf generate a quiz.
    quiz_blueprint = {}

    # PROMPTS

    quiz_blueprint["uni_name"] = input("University (type nothing to ignore): ")
    quiz_blueprint["college"] = input("College (type nothing to ignore): ")
    quiz_blueprint["dept"] = input("Department (type nothing to ignore): ")
    quiz_blueprint["course"] = input("Course (type nothing to ignore): ")

    while(True):
        if(duration := check_valid_num( input("Duration (minutes, type '0' to ignore): ") )):
            quiz_blueprint["duration"] = int(duration)
            break
        else:
            print("!!! Please re-enter a valid duration.")
            continue



    quiz_blueprint["ask_name"] = True if (input("[yes/no] require Name? ").lower() == "yes") else None
    quiz_blueprint["ask_id"] = True if (input("[yes/no] require ID? ").lower() == "yes") else None

    # user can enter as many lines as he wishes to add as an extra part, he can include rules, tips, restrictions, etc...
    extra_input = input("Anything you would like to add? (ex. Rules, Tips, etc..), type nothing when done adding: \n~ ")
    quiz_blueprint["extra_part"] = []
    while(extra_input):
        quiz_blueprint["extra_part"].append(extra_input)
        extra_input = input("~ ")



# MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ
# MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ MCQ

    # static variables
    quiz_blueprint["mcq_questions"] = []
    quiz_blueprint["total_mcq_weight"]: float = 0.0

    # HOW MANY MCQ QUESTIONS ?:
    while(True):
        try:
            mcq = int(input("How many MCQs' are on the quiz?: "))
            # not having any mcqs' on the quiz is acceptable
            if (mcq<0): raise ValueError
        except ValueError:
            print("!!! Please re-enter a number greater than or equal 0.")
            continue
        else:
            break

    # START OF MCQ LOOP
    # here we create an mcq by prompting the user to eneter info (weight, text, choices)
    for q in range(mcq):

        # help the quiz creator know which question he's building
        question_ordinal = inflect.engine().number_to_words(inflect.engine().ordinal(q+1))

        # DISPLAY MCQ NUMBER
        print(f"\n~ {question_ordinal.capitalize()} MCQ ")

        # MCQ WEIGHT
        mcq_weight: float = None
        while(True):
            if  (mcq_weight := check_valid_num(input("\tEnter weight: "))):
                # adding the weight to the total_mcq_weight
                quiz_blueprint["total_mcq_weight"] += mcq_weight
                break
            else:
                print("\t!!! Please re-enter a valid weight.")
                continue

        # MCQ TEXT
        mcq_txt = input("\tEnter question text: ")

        # MCQ CHOICES
        mcq_choices = []
        while(True):
            try:
                num_of_choices = int(input("\tHow many choices? "))
                # any mcq must have atleast 2 choices
                if(num_of_choices < 2): raise ValueError

                i = 1
                for q in range(num_of_choices):
                    choices_ordinal = inflect.engine().number_to_words(inflect.engine().ordinal(q+1))
                    mcq_choices.append(input(f"\t\tEnter {choices_ordinal} choice: "))
                    i += 1
            except ValueError:
                print("\t!!! Any MCQ must have at least two choices.")
                continue
            else:
                break


        # appending the current mcq we just finished creating into the list of objects "mcq_questions"
        quiz_blueprint["mcq_questions"].append(MCQ(mcq_weight, mcq_txt, mcq_choices))

        # END OF MCQ LOOP

# ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY
# ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY ESSAY

    # static variables
    quiz_blueprint["essay_questions"] = []
    quiz_blueprint["total_essay_weight"] = 0

    # HOW MANY Essay QUESTIONS ?:
    while(True):
        try:
            essay = int(input("How many Essays' are on the quiz?: "))
            # not having any essays' on the quiz is acceptable
            if (essay<0): raise ValueError
        except ValueError:
            print("!!! Please re-enter a number greater than or equal 0.")
            continue
        else:
            break


    for e in range(essay):
        # help the quiz creator know which question he's building
        question_ordinal = inflect.engine().number_to_words(inflect.engine().ordinal(e+1))

        # DISPLAY Essay NUMBER
        print(f"\n~ {question_ordinal.capitalize()} Essay: ")

        # Essay WEIGHT
        essay_weight = None
        while(True):
            if  (essay_weight := check_valid_num(input("\tEnter weight: "))):
                # adding the weight to the total_essay_weight

                if type(essay_weight) != bool:
                    # add to total weight only if it was an int, >0
                    quiz_blueprint["total_essay_weight"] += essay_weight
                break
            else:
                print("\t!!! Please re-enter a valid weight.")
                continue

        # Essay TEXT
        essay_txt = input("\tQuestion text: ")

        # Essay answer area size
        essay_lines = None
        while(True):
            try:
                essay_lines = int(input("\tHow many lines needed for the answer? "))
                # any essay answer must have atleast 1 lines
                if(essay_lines < 1):
                    print("\t!!! Any essay answer must have at least one line.")
                    raise ValueError
            except ValueError as e:
                print("\t!!! Please re-enter a valid number.")
                continue
            else:
                break

        # Essay, answer area has lines or no
        essay_has_lines = True if (input("\t[yes/no] include lines in the answer area: ").lower() == "yes") else None


        # appending the current essay we just finished creating into the list "essay_questions"
        quiz_blueprint["essay_questions"].append(Essay(essay_weight, essay_txt, essay_lines, essay_has_lines))
        # END OF Essay LOOP







# ////////////////////////// END OF PROMPTING //////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # initialize the quiz with the previously populated dictionary
    quiz = initialize_quiz(quiz_blueprint)

    # pdf.output(f"{file_name}.pdf")
    generate_quiz(quiz, file_name)

def check_valid_num(x):
    """checks wether a valid number was entered when prompted"""
    try:
        number = float(x)
        if(number < 0): raise ValueError
        if(number > 0): return float(x)
        if(number == 0): return True    # if it is zero, i want it to return True to activate the if statement
    except ValueError:
        # means it is not an integer
        return False

def initialize_quiz(quiz_blueprint):
    return Quiz(quiz_blueprint)

def generate_quiz(q: Quiz ,file_name):
    # Start the pdf for the quiz
    pdf = PDF()
    pdf.add_page()

    # Add the header
    pdf.desc(q)

    # Add the MCQ PART
    pdf.add_mcq_part(q)

    # Add the Essay PART
    pdf.add_essay_part(q)

    # output the quiz.
    pdf.output(f"{file_name}.pdf")




if __name__ == "__main__":
    main()