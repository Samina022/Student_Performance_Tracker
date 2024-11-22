class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        if name in self.students:
            print(f"Student {name} already exists. Updating scores.")
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_scores = sum(student.calculate_average() for student in self.students.values())
        return total_scores / len(self.students)

    def display_student_performance(self):
        print("\nStudent Performance Report:\n")
        for student in self.students.values():
            average = student.calculate_average()
            status = "Pass" if student.is_passing() else "Fail"
            print(f"Name: {student.name}, Average: {average:.2f}, Status: {status}")

        class_avg = self.calculate_class_average()
        print(f"\nClass Average: {class_avg:.2f}")


def main():
    tracker = PerformanceTracker()

    while True:
        print("\nEnter student details (or type 'done' to finish):")
        name = input("Student Name: ").strip()
        if name.lower() == "done":
            break

        try:
            scores = []
            for subject in ["Math", "Science", "English"]:
                score = int(input(f"Enter score for {subject}: "))
                scores.append(score)
            tracker.add_student(name, scores)
        except ValueError:
            print("Invalid input! Please enter numeric values for scores.")
            continue

    tracker.display_student_performance()


if __name__ == "__main__":
    main()
