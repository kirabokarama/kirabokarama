marks = [[56,89,70,92,67,100],[60,70,100,45,70,76],[60,95,90,85,93,45],[55,80,56,45,51,76],[78,100,65,77,91,87],
[45,78,65,50,45,87],[32,50,45,67,40,80]]
students = ["Peter","Jackson","Valentin","Pamela","Jean Paul","Ahmed","Kellen"]
subjects = ["Algorighms and Data Structures","Java","Web AppDevelopment","Databases", "Human Computer Interaction","Information Retrieval"]
# Calculating an average of how student pass in each subject 
#to calculate the subject average to the best performing course 
marks = [[56,89,70,92,67,100],[60,70,100,45,70,76],[60,95,90,85,93,45],[55,80,56,45,51,76],[78,100,65,77,91,87],
[45,78,65,50,45,87],[32,50,45,67,40,80]]
subject_average = [sum(sub_list) / len(sub_list) for sub_list in zip(*marks)]
student_average = [sum(sub_list) / len(sub_list) for sub_list in marks]

subject={

    subject_average[0]: subjects[0],
    subject_average[1]: subjects[1],
    subject_average[2]: subjects[2],
    subject_average[3]: subjects[3],
    subject_average[4]: subjects[4],
    subject_average[5]: subjects[5],
 

}
