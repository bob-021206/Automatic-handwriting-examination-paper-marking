# Automatic-handwriting-examination-paper-marking
This project includes programs could be used to grade your handwriting codes by given standard answers. You can follow the readme file to use it easily.
Step1: Take a picture of each question and put them into the same folder. Type the path of the folder here. Make sure each picture is named as “student’s name_ Question number”, such as “San Zhang_Q1.jpg”
 
Step1: change the folder path
Step2: check the output path of Nanonets and run the “API_upload” code.
Step3: The recognized answer will be outputted to google sheet. Then we download it to the local folder. Also, we put the standard answer excel in the same folder and change the path in the “Auto-grading System v2.0” code.

Result will be shown in the same excel file of the Nanonets data. There will be a new sheet for it, following the order of the questions on the original sheet.

The results show that for those well written answers, the AI model could give a clear recognition and the final grading could be done successfully. While for those in poor handwriting, the recognition of AI model will have some mistakes. Sometimes these mistakes will cause an unwanted deduction of points. We still need to improve the recognition part for a better accuracy.
