"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    rounded_scores = []

    for score in student_scores:
        rounded_scores.append(round(score))

    return rounded_scores

    


def count_failed_students(student_scores):
    count=0
    for item in student_scores:
        if item<=40:
            count=count+1
    return count

def above_threshold(student_scores, threshold):
     the_best=[]
     for item in student_scores:
         if item >= threshold:
            the_best.append(item)
     return the_best

def letter_grades(highest):
    increment_variable=(highest-40)/4
    grade_list=[41,int(41+increment_variable),int(41+increment_variable*2),int(41+increment_variable*3)]
    return grade_list

def student_ranking(student_scores, student_names):
    new_list = []

    for item in range(len(student_scores)):
        new_list.append(
            f"{item + 1}. {student_names[item]}: {student_scores[item]}"
        )

    return new_list

def perfect_score(student_info):
    perfect_list=[]
    for name,score in student_info:
        if score==100:
           perfect_list.extend([name,score])
           break

    return perfect_list
