import firebase_admin
from firebase_admin import credentials, firestore
import xlrd
from pyasn1.compat.octets import null

path = "./Updated Time Table, FAST School of Computing, Fall 2020 (1).xlsx"
inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(3)
#print("rows: ",inputWorksheet.nrows)
#print("col: ",inputWorksheet.ncols)




cred = credentials.Certificate('./fyp-2-3e464-firebase-adminsdk-1hgpf-1af6de1809.json')
defaultapp = firebase_admin.initialize_app(cred)

db = firestore.client()
rowc = 0
for x in range(6, 35):
    rowc = rowc + 1
    print(rowc)
    #print(inputWorksheet.cell_value(x, 2))
    room = inputWorksheet.cell_value(x, 2)
    print("room:",room)
    for y in range(3, inputWorksheet.ncols):
        timing = inputWorksheet.cell_value(5, y)

        if(len(timing) > 0):
            print("timing:", timing)
            subject = inputWorksheet.cell_value(x,y)
            print("subject:",subject)

            if(len(subject) > 1):
                doc_ref = db.collection('d').document(subject)
                doc = doc_ref.get()
                print(doc.exists)
                if(doc.exists):
                    print("hi")
                    doc_ref = db.collection('d').document(subject)
                    doc_ref.set({
                        "Room2": room,
                        "Timing2": timing
                    },merge=True)


                else:
                    print("heloooooooo")
                    doc_ref = db.collection('d').document(subject)
                    doc_ref.set({
                        "Room1": room,
                        "Timing1": timing
                    })

            else:
                pass





