from fpdf import FPDF
from quiz import Quiz


class PDF(FPDF):

    def desc(self, quiz: Quiz):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 11)

        if quiz.uni_name:
            # Printing University's name:
            self.cell(0, 0, quiz.uni_name, border=0, align="C")
            self.ln(5)

        if quiz.college:
            # Printing college name:
            self.cell(0, 0, quiz.college, border=0, align="C")
            self.ln(5)

        if quiz.dept:
            # Printing department name:
            self.cell(0, 0, quiz.dept, border=0, align="C")
            self.ln(5)

        if quiz.course:
            # Printing course id - name:
            self.cell(0, 0, quiz.course, border=0, align="C")
            self.ln(5)


        if type(quiz.duration) != bool and quiz.duration > 0:
            # Printing quiz duration:
            self.set_font("helvetica", "I", 8)
            self.cell(0, 0, f"Quiz duration: {quiz.duration} minutes", border=0, align="C")
            self.ln(5)


        self.ln(5)
        # asking for the name and id
        name_id: str = ""

        # if name is needed, add it
        if(quiz.ask_name):
            name_id += "Name:  ___________________________"

        # if ID is needed add it
        if(quiz.ask_id):
            # if name wasn't asked, don't add the separation
            if(name_id != ""): name_id += "                    "
            name_id += "ID:  ___________________________"

        if name_id:
            self.set_font("helvetica", "I", 8)
            self.cell(0,0, name_id, align="C")
            self.ln(8)


        if quiz.extra_part:
            # Printing extra lines, chosen by the examinator:
            self.set_font("helvetica", "I", 8)
            for line in quiz.extra_part:
                self.ln()
                self.write(4, f"- {line}")

            self.ln(8)



        total_quiz_weight = quiz.total_mcq_weight + quiz.total_essay_weight
        # if the weight of this part is a whole number, print it without the decimal:
        if (total_quiz_weight % 1) == 0:
            total_quiz_weight = int(total_quiz_weight)

        # Divider line
            # the margin that the border never covers is 10 mm left and right (total 20). wdith of A4 is 210mm
        self.cell(20)
        right_padding = 150 #default
        if(total_quiz_weight > 0): right_padding -= 15 # to make space for the total weight
        self.cell(right_padding,0, border="B", align="L", ln=0)
        # self.ln(10)



        # if total weight is > than 0 print it
        if total_quiz_weight > 0:
            self.set_font("helvetica", "B", 11)
            self.cell(0, 0, f"[            / {total_quiz_weight} ]", border=0, align="R")
        self.ln(10)


# # ///////////////////////////////////// END OF HEADER ///////////////////////////////////////////////////////////////////////

    def add_mcq_part(self, q: Quiz):
        self.set_font("helvetica", "B", 12)

        # Printing MCQ part title if we have a mcq
        if len(q.mcq_questions) > 0:
            self.set_font("helvetica", "B", 10)
            self.cell(0, 0, "Multiple-choice Questions", align="C")

            # if the weight of this part is a whole number, print it without the decimal:
            if (Quiz.total_mcq_weight % 1) == 0: Quiz.total_mcq_weight = int(Quiz.total_mcq_weight)

            self.cell(0, 0, f"[        / {Quiz.total_mcq_weight} ]", align="R")
        else: return




        self.set_font("helvetica", "", 11)

        # looping through every mcq in the quiz
        for q in Quiz.mcq_questions:
            # PRINTING THE QUESTION with index
            self.write(6, f"{Quiz.mcq_questions.index(q)+1}) {q.txt}\n")
            self.ln(2)

            # looping through the choices
            chr_index = 65 #this is used to conver numbers to letters: 1:A, 2:B, ...
            for choice in q.choices:
                # PRINTING THE CHOICE with index if exists
                if choice:
                    self.write(6, f"        ({chr(chr_index)})  {choice}\n")
                    chr_index += 1 # increment to go to next letter

            # add space after question
            self.ln(6)


        # Divider line
        # the margin that the border never covers is 10 mm left and right (total 20)
        self.cell(15)
        self.cell(160,0, border="B", align="C")
        self.ln(10)




    def add_essay_part(self, q: Quiz):
        # Printing Essay part title if we have an essay with the total weight
        if len(q.essay_questions) > 0:
            self.set_font("helvetica", "B", 10)
            self.cell(0, 0, "Essay Questions", align="C")

            if(Quiz.total_essay_weight != 0):
                # if the weight of this part is a whole number, print it without the decimal:
                if (Quiz.total_essay_weight % 1) == 0: Quiz.total_essay_weight = int(Quiz.total_essay_weight)
                self.cell(0, 0, f"[        / {Quiz.total_essay_weight} ]", align="R")
            self.ln(10)
        else:
            return




        # looping through every essay question
        for q in Quiz.essay_questions:
            if(type(q.weight) != bool and q.weight > 0):

                self.set_font("helvetica", "I", 9)
                self.cell(0, 0, f"Essay {Quiz.essay_questions.index(q)+1}", align="L")

                # weight
                self.set_font("helvetica", "", 10)

                # if the weight of this part is a whole number, print it without the decimal:
                if (q.weight % 1) == 0: q.weight = int(q.weight)
                self.cell(0, 0, f"[        / {q.weight} ]", align="R")

            # Question txt
            self.set_font("helvetica", "", 11)
            self.write(5, f"{q.question}\n")
            for i in range(q.lines):
                self.ln(8)
                # prints lines for the examinee to write over
                if q.has_lines:
                    self.cell(5)
                    self.cell(0,0,"",border="B")

            # add space after question
            self.ln(15)