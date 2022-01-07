from resume_parser import resumeparse

data = resumeparse.read_file("Amit_Sharma_Resume.pdf")

for i, j in data.items():
    print(f"{i}:---->{j}")