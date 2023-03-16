
class Quiz:
    def __init__(self, quiz_blueprint):

        self.uni_name           = quiz_blueprint["uni_name"]
        self.college            = quiz_blueprint["college"]
        self.dept               = quiz_blueprint["dept"]
        self.course             = quiz_blueprint["course"]
        self.duration: int      = quiz_blueprint["duration"]
        self.ask_name: bool     = quiz_blueprint["ask_name"]
        self.ask_id: bool       = quiz_blueprint["ask_id"]
        self.extra_part = quiz_blueprint["extra_part"]


        # for MCQ
        Quiz.mcq_questions: MCQ = quiz_blueprint["mcq_questions"]
        Quiz.total_mcq_weight = quiz_blueprint["total_mcq_weight"]

        # for Essay
        Quiz.essay_questions: Essay = quiz_blueprint["essay_questions"]
        Quiz.total_essay_weight = quiz_blueprint["total_essay_weight"]







class MCQ:

    def __init__(self, weight, txt, choices: list):
        self.weight: int = weight
        self.txt = txt
        self.choices = choices


    def __str__(self) -> str:
        weight = self.weight
        txt = self.txt
        choices = self.choices

        return f"_______________\nWeight = {weight}\nText = {txt}\nChoices : {choices}"





class Essay:

    def __init__(self, weight, question, lines, has_lines):
        self.weight = weight
        self.question = question

        # the size of the answer area
        self.lines = lines

        # lines for writing over
        self.has_lines = has_lines



    def __str__(self) -> str:
        weight = self.weight
        question = self.question
        lines = self.lines
        has_lines = self.has_lines

        return f"_______________\nWeight: {weight}\nQuestion: {question}\nNumber of lines: {lines}\nHas lines: {has_lines}"


