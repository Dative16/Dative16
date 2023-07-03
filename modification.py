from tkinter import *
from tkinter import ttk
from tkinter import Tk
import random
import time
import datetime
from tkinter import Button


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white",
                         font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # ============================= DATAFRAME======================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                   font=("arial", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("arial", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # ================================= BUTTONS FRAME==============================

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=540, width=1530, height=70)  # Adjusted y-coordinate

        # ================================ DETAILS FRAME==============================

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=610, width=1530, height=190)

        # =============================== Dataframeleft ===============================

        lblNameTablet = Label(DataframeLeft, text="Names of Table", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0, sticky=W)

        comNameTablet = ttk.Combobox(DataframeLeft, state="readonly",
                                     font=("arial", 12, "bold"), width=33)
        comNameTablet["values"] = ("Nice", "Corona Vacacine", "Acetaminophen", "Adderall", "Amiodipine", "Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Refence No:", pady=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(DataframeLeft, font=("arial", 12, "bold"), text="No of Tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)

        lblEDailyDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblEDailyDose.grid(row=7, column=0, sticky=W)
        txtDailDose = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtDailDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFutherinfo = Label(DataframeLeft, font=("arial", 12, "bold"), text="Futher Information:", padx=2)
        lblFutherinfo.grid(row=0, column=2, sticky=W)
        txtFutherinfo = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtFutherinfo.grid(row=0, column=3)

        lblBloodPressuer = Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2)
        lblBloodPressuer.grid(row=1, column=2, sticky=W)
        txtBloodPressuer = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtBloodPressuer.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, font=("arial", 12, "bold"), text="Medication:", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtMedicine.grid(row=3, column=3, sticky=W)

        lblPatientId = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Id:", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientname = Label(DataframeLeft, font=("arial", 12, "bold"), text="Parient Name:", padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtPatientname.grid(row=6, column=3)

        lblDataOfBirth = Label(DataframeLeft, font=("arial", 12, "bold"), text="Data of Birth:", padx=2, pady=6)
        lblDataOfBirth.grid(row=7, column=2, sticky=W)
        txtDataOfBirth = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtDataOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtPatientAddress.grid(row=8, column=3)

        # ================================================== Data Frame Right ==================================
        self.txtPresciption = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPresciption.grid(row=0, column=0)

        # ============================================= Bouttons ==========================================
        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=23, height=16, padx=2, pady=6)

        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white",
                                     font=("arial", 12, "bold"),
                                     width=23, height=16, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"),
                           width=23, height=16, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"),
                           width=23, height=16, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"),
                          width=23, height=16, padx=2, pady=6)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"),
                         width=23, height=16, padx=2, pady=6)
        btnExit.grid(row=0, column=5)


root = Tk()
ob = Hospital(root)
root.mainloop()