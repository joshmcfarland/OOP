import PatientClass as pat
import ProcedureClass as pro

patient_id = 1
name = "Matt Jones"
address = "123 Main st, Waco TX 76706"
phone = "254-555-7415"
veteran_status = True

patient = pat.Patient(patient_id, name, address, phone, veteran_status)

proc_name = "Physical Exam"
date = "2/15/2022"
pract_name = "Dr. Irvine"
charges = 250
patient_id = 1

proc_name = "MRI"
date = "2/15/2022"
pract_name = "Dr. Hamilton"
charges = 1500
patient_id = 1

proc_name = "CT Scan"
date = "2/17/2022"
pract_name = "Dr. Drey"
charges = 1200
patient_id = 2

procedure = pro.Procedure(proc_name, date, pract_name, charges, id)


def main():
    if patient.get_id == procedure.get_ID:
        print(patient.get_id())
        print(patient.get_name())
        print(patient.get_address())
        print(patient.get_phone())
        print(patient.get_veteran_status())

        print(procedure.get_proc_name())
        print(procedure.get_date())
        print(procedure.get_pract_name())
        print(procedure.get_charges())
        print(procedure.get_id())


main()
