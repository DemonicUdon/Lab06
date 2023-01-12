
class CalUtils:
    def __init__(self):
        self.names = list()
        self.heights = list()
        self.total_student_count = 0
        self.total_student_height = 0.0

    def CalAvgHeight(self):
        f = open('listOfStudentHeight.txt', "r")
        for i in f:
            self.names.append(i.split()[0])
            self.heights.append(i.split()[1])
            self.total_student_count += 1
            self.total_student_height += float(i.split()[1])
        f.close()
        print(self.names)
        print(self.heights)
        print("Combined student height is: {:.2f} ".format(self.total_student_height))
        print("Number of students: ", self.total_student_count)
        Average = self.total_student_height / self.total_student_count
        print("Aggregate student height is: {:.2f}m".format(Average))
        self.Add()

    def Add(self):
        volt = open("listOfStudentHeight.txt", "a")
        self.total_student_count = 0
        self.total_student_height = 0
        new_name = input("Enter the new face: ")
        heights = 0
        while True:
            try:
                heights = float(input("Enter the giant's height: "))
                break
            except:
                print("Please input a valid planet height.")

        volt.write("\n")
        volt.write(new_name)
        volt.write("   ")
        volt.write(str(heights))
        volt.close()
        return(self.CalAvgHeight())


myClass = CalUtils()
myClass.CalAvgHeight()

