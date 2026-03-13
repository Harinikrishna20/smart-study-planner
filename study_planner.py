subjects = int(input("Enter number of subjects: "))

subject_names = []
chapters = []

for i in range(subjects):
    name = input("\nEnter subject name: ")
    total_chapters = int(input("Enter total chapters in " + name + ": "))
    
    subject_names.append(name)
    chapters.append(total_chapters)

days_left = int(input("\nEnter number of days left for exam: "))
chapters_per_hours = float(input("\nHow many chapters can you study per hours: "))
hours_per_day=float(input("\nhow many hours do u study in a day"))

print("\nSYLLABUS COMPLETION PREDICTION\n")
chapter_per_day=chapters_per_hours*hours_per_day
for i in range(subjects):
    days_needed = chapters[i] / chapter_per_day
    
    print("Subject:", subject_names[i])
    print("Days needed:", round(days_needed,2))
    
    if days_needed <= days_left:
        print("Status: You can complete the syllabus ✅")
    else:
        print("Status: Not possible to complete ❌")
    
    print()