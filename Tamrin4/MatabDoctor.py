class Patient:
    def __init__(self, id, name, familyname, age, height, weight):
        self.id = id
        self.name = name
        self.familyname = familyname
        self.age = age
        self.height = height
        self.weight = weight


class Appointment:
    patient_list = dict()
    timetable = dict()

    def add_patient(self, id, name, familyname, age, height, weight):
        if int(id) in Appointment.patient_list:
            print("error: this ID already exists")
        elif int(age) < 0:
            print("error: invalid age")
        elif int(height) < 0:
            print("error: invalid height")
        elif int(weight) < 0:
            print("error: invalid weight")
        else:
            Appointment.patient_list[int(id)] = Patient(int(id), name, familyname, int(age), int(height), int(weight))
            print("patient added successfully")

    def display_patient(self, id):
        if int(id) not in Appointment.patient_list:
            print("error: invalid ID")
        else:
            print(f"patient name: {Appointment.patient_list[int(id)].name}")
            print(f"patient family name: {Appointment.patient_list[int(id)].familyname}")
            print(f"patient age: {Appointment.patient_list[int(id)].age}")
            print(f"patient height: {Appointment.patient_list[int(id)].height}")
            print(f"patient weight: {Appointment.patient_list[int(id)].weight}")

    def add_visit(self,id, beginning_time):
        if int(id) not in Appointment.patient_list:
            print("error: invalid id")
        elif not 9 <= int(beginning_time) <= 18:
            print("error: invalid time")
        elif int(beginning_time) in Appointment.timetable:
            print("error: busy time")
        else:
            Appointment.timetable[int(beginning_time)] = int(id)
            print("visit added successfully!")

    def delete_patient(self,id):
        if int(id) not in Appointment.patient_list:
            print("error: invalid id")
        else:
            del Appointment.patient_list[int(id)]
            print("patient deleted successfully!")
            Appointment.timetable = {time: int(iid) for time, iid in Appointment.timetable.items() if int(iid) != int(id)}

    def display_visit_list(self):
        print("SCHEDULE:")
        for time, id in Appointment.timetable.items():
            print(f"{time}:00", f"{Appointment.patient_list[id].name}", f"{Appointment.patient_list[id].familyname}")
x = Appointment()
while True:
    command = input()
    if command == "exit":
        break
    command = command.split()
    if not command:
        print("invalid command")
    else:
        if "add" == command[0] and "patient" == command[1]:
            x.add_patient(command[2], command[3], command[4], command[5], command[6], command[7])
        elif "display" == command[0] and "patient" == command[1]:
            x.display_patient(command[2])
        elif "add" == command[0] and command[1] == "visit":
            x.add_visit(command[2], command[3])
        elif "delete" ==command[0] and command[1] == "patient":
            x.delete_patient(command[2])
        elif "display" == command[0] and "visit" == command[1] and "list" == command[2]:
            x.display_visit_list()

        else:
            print("invalid command")


