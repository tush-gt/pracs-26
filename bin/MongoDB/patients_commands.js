// Run these commands inside mongosh, not in the Linux terminal.
use Hospital
db.createCollection("Patients")
db.Patients.insertOne({patient_id: 101, name: "Asha", age: 35, disease: "Fever", fees: 500})
db.Patients.insertMany([
  {patient_id: 102, name: "Ravi", age: 42, disease: "Diabetes", fees: 1200},
  {patient_id: 103, name: "Neha", age: 28, disease: "Fever", fees: 700},
  {patient_id: 104, name: "Kiran", age: 55, disease: "BP", fees: 1500},
  {patient_id: 105, name: "Meera", age: 31, disease: "Asthma", fees: 900}
])
db.Patients.find()
db.Patients.find({patient_id: 103})
db.Patients.find({disease: "Fever"})
db.Patients.find({fees: {$gt: 800}})
db.Patients.find({$and: [{age: {$gt: 30}}, {fees: {$gt: 700}}]})
db.Patients.find({$or: [{disease: "Fever"}, {disease: "BP"}]})
db.Patients.find({}, {_id: 0, name: 1, disease: 1})
db.Patients.find().sort({fees: -1})
db.Patients.updateOne({patient_id: 101}, {$set: {disease: "Recovered"}})
db.Patients.updateMany({disease: "Fever"}, {$set: {status: "Under Observation"}})
db.Patients.updateMany({}, {$inc: {fees: 100}})
db.Patients.deleteOne({patient_id: 105})
db.Patients.deleteMany({fees: {$gt: 1500}})
db.Patients.find()
db.Patients.countDocuments()
