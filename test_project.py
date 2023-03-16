from project import check_valid_num, initialize_quiz, generate_quiz
from quiz import Quiz, MCQ, Essay
from os.path import exists



def test_check_valid_num():
    """ tests the method that validates input
    reject: negative numbers and strings. Return True when number is zero"""
    assert check_valid_num(9) == 9
    assert check_valid_num("1000") == 1000
    assert check_valid_num(0) == True
    assert check_valid_num(-10) == False
    assert check_valid_num("string") == False
    assert check_valid_num("Fail") == False


mcq1 = MCQ(1, "What is 1 + 1?: ", ['1', '2', 'test'])
mcq2 = MCQ(1, "What is a potato?: ", ['fruit', 'vegetable', 'insect'])
essay1 = Essay(5, "Draw a ladybug: ", 5, False)
essay2 = Essay(5, "What is the capital of Algeria: ", 1, True)

quiz_dict = {
        'uni_name': 'ABC University',
        'college': 'CCIS',
        'dept': 'IS',
        'course': 'IS201 - Intro to Information Systems',
        'duration': 90,
        'ask_id': True,
        'ask_name': True,

        'mcq_questions': [mcq1, mcq2],
        'essay_questions': [essay1, essay2],

        # must find solution
        'total_mcq_weight': 2,
        'total_essay_weight': 10,

        'extra_part': ['Do not use a calculator', 'Only use blue pen or pencil']
                }

def test_initialize_quiz():
    """This test checks if the dictionary, populated by the user, was successfully coppied"""
    q = initialize_quiz(quiz_dict)
    assert q.uni_name   == "ABC University"
    assert q.college    == "CCIS"
    assert q.dept       == "IS"
    assert q.course     == "IS201 - Intro to Information Systems"
    assert q.duration   == 90
    assert q.ask_name   == True
    assert q.ask_id     == True
    assert q.extra_part == ['Do not use a calculator', 'Only use blue pen or pencil']

    assert Quiz.mcq_questions == [q for q in Quiz.mcq_questions]
    assert Quiz.total_mcq_weight == sum([q.weight for q in Quiz.mcq_questions])


    assert Quiz.essay_questions == [q for q in Quiz.essay_questions]
    assert Quiz.total_essay_weight == sum([q.weight for q in Quiz.essay_questions])




def test_generate_quiz():
    """This test checks if the quiz was successfully generated and no errors happened"""
    q = initialize_quiz(quiz_dict)
    file_name = "test"

    generate_quiz(q, file_name)

    assert exists(f"{file_name}.pdf") == True