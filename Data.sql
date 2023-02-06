insert into Customer(UserName,LicenseNo,Firstname,Lastname,Password,email,DOB,Address,Phone_no,Gender)
values
    ("123@123","DL-04056789778","H","Hemanth","123@123","Hemanth.123@gmail.com","2000-02-04","Church Street,Bengaluru,India","8322335011","Male"),
    ("124@124","DL-04056789999","A","Revanth","124@124","Revanth@gmail.com","2002-03-23","Church Street,Bengaluru,India","7886870547","Male"),
    ("125@125","DL-04075789999","B","Anil","125@125","Anil@gmail.com","2002-04-08","Jayanagar,Bengaluru,India","9845123645","Male"),
    ("126@126","DL-04075781234","C","Sunitha","126@126","Sunitha@gmail.com","2001-07-21","Majestic,Bengaluru,India","7643123456","Female"),
    ("127@127","DL-79975781234","F","Suman","127@127","Suman@gmail.com","2001-05-22","White Field,Bengaluru,India","2345312672","Male"),
    ("128@128","DL-79975781265","I","Sumantha","128@128","Sumantha@gmail.com","2000-03-01","K.R Puram,Bengaluru,India","9745312768","Female"),
    ("129@129","DL-12398781234","P","Pushpika","129@129","Pushpika@gmail.com","1995-10-10","Kengeri,Bengaluru,India","9623915687","Female"),
    ("130@130","DL-7994531234","O","Teja","130@130","Teja@gmail.com","2003-09-06","Jayanagar,Bengaluru,India","7532167985","Female"),
    ("131@131","DL-77777777777","MS","Dhoni","131@131","Dhoni@gmail.com","19877-02-18","Church Street,Bengaluru,India","6754287906","Male"),
    ("132@132","DL-79975782734","Virat","Kohli","132@132","Kohli@gmai.com","1988-10-18","MG Rd,Bengaluru,India","4538329876","Male");

--Location
Insert into Location(state,city,Area,pincode)
values
    ("Karnataka","Bengaluru","Kempegowda International Airport","583101"),
    ("Karnataka","Bengaluru","Pes University","560085"),
    ("Karnataka","Bengaluru","Palace Grounds","560063"),
    ("Karnataka","Bengaluru","KSR Railway Station","560085" ),
    ("Karnataka","Bengaluru","Majestic Bus Station","560034"),
    ("Karnataka","Bengaluru","Church Street","560007");




--Car Category
insert into car_category(
    category_name,
    no_of_persons,
    cost_per_day,
    Delay_Fee_per_hour
)
values
    ('ECONOMY', 5, 30, 0.9),
    ('STANDARD', 5, 38, 1.14),
    ('MINI VAN', 7, 70, 2.1),
    ('FULL SIZE SUV', 8, 60, 1.8);

--Insert using CSV format:
-- LOAD DATA INFILE "data2.csv" INTO TABLE car_category
-- COLUMNS TERMINATED BY ","
-- OPTIONALLY ENCLOSED BY ""
-- ESCAPED BY ""
-- LINES TERMINATED BY "\n"
-- IGNORE 1 LINES;

--car Details:
insert into car_detail(Registration_No,Model,Make,Model_Year,Mileage,Category,Location)
values
    ('DA6523','CIVIC','HONDA',2014,9,'ECONOMY',6003),
    ('FA1252','BOLT','CHEVORLET',2015,7,'ECONOMY',6001),
    ('GQ2146','INSIGHT','HONDA',2016,6.5,'ECONOMY',6002),
    ('VR2341','COROLLA','TOYOTA',2014,12.356,'ECONOMY',6004),
    ('KS1683','TIAGO','TATA',2014,8,'STANDARD',6005),
    ('HNX1890','PRIUS','TOYOTA',2015,7.8,'STANDARD',6002),
    ('UI1289','TRIBER','RENAULT',2017,6,'MINI VAN',6003),
    ('OP9867','ERTIGA','MARUTHI',2018,8,'MINI VAN',6005),
    ('UI7745','INNOVA CRYSTA','TOYATA',2020,8,'FULL SIZE SUV',6004);

--Insert Data using Another Variation : 
insert into car_detail values
    ("RA9867","FIG0","FORD",2018,8,1,"STANDARD",6004),
    ('OU7023','CRUZE','CHEVROLET',2016,7,1,'MINI VAN',6002);

--Car Insurance
insert into Car_Insurance(Insurance_Name,Coverage_Type,Insurance_Cost_Per_Day)
values
    ('Collision Damage Waiver','Bodywork of the Car,Additional parts',3),
    ('Personal Accident','IF you get Injured',2),
    ('Roadside Assistance','IF the car breaks Down',2);


--Payment
insert into Payment(Total_Amount,Payment_Method)
values
(0,"Debit"),
(1000,"Debit"),
(2000,"Credit"),
(1500,"Cash"),
(10000,"UPI"),
(0,"Credit"),
(0,"Credit");

--Booking
insert into Booking_Details(Customer_ID,From_Date,Return_Date,Amount,Actual_Return_Date,Pickup_Location,Drop_Location,Insurance,Car_Reg_No,Payment_ID)
values
    (5000,"2022-11-07","2022-11-10 07:00",0,"2022-11-11 07:00",6000,6000,7000,"KS1683",8000),
    (5001,"2022-11-08","2022-11-11 08:00",0,"2022-11-11 10:00",6001,6001,7001,"UI7745",8000),
    (5002,"2022-10-07","2022-10-14 15:00",0,"2022-10-15 10:00",6002,6002,7000,"DA6523",8000),
    (5003,"2022-10-20","2022-10-28 17:00",0,"2022-10-28 17:00",6003,6000,7000,"HNX189",8000),
    (5004,"2022-10-29","2022-11-05 10:00",0,"2022-11-05 13:00",6004,6000,7002,"OP9867",8000),
    (5005,"2022-11-14","2022-11-20 9:00",0,"2022-11-20 9:00",6000,6003,7001,"UI1289",8000);
