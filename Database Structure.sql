--Creating Customer
create table Customer(
    Customer_ID int not null auto_increment primary key,
    UserName varchar(35) not null unique,
    LicenseNo varchar(35) not null,
    Firstname varchar(35) not null,
    Lastname varchar(35) not null,
    Password varchar(50) not null,
    email varchar(35),
    DOB date not null,
    Address varchar(50),
    phone_no char(10) not null,
    Gender varchar(10) not null,
    constraint check_phone_customer check(char_length(phone_no) = 10)
);

alter table Customer auto_increment = 5000;

--Creating Location
create table Location(
    Location_ID int not null auto_increment primary key,
    state varchar(35) not null,
    city varchar(35) not null,
    Area varchar(35) not null,
    pincode char(6) not null,
    constraint pincode_invalid check(char_length(pincode) = 6)
    );

alter table Location auto_increment = 6000;

--Creating Car Category
create table car_category(
    category_name varchar(35) not null primary key,
    no_of_persons int not null,
    cost_per_day double not null,
    Delay_Fee_per_hour double not null
);

--Creating Car
create table car_detail(
    Registration_No char(6) not null primary key,
    Model varchar(35) not null,
    Make varchar(35) not null,
    Model_Year int(4) not null,
    Mileage double not null,
    Availability boolean default true,
    Category varchar(35) not null,
    Location int not null,
    foreign key(Category) references car_category(category_name),
    foreign key(Location) references Location(Location_ID)
);

--Creating Insurance
create table Car_Insurance(
    Insurance_ID int not null auto_increment primary key,
    Insurance_Name varchar(35) not null,
    Coverage_Type varchar(35) not null,
    Insurance_Cost_Per_Day double not null
    );

alter table Car_Insurance auto_increment = 7000;

--Creating Payment
create table Payment(
    Payment_ID int not null auto_increment primary key,
    Total_Amount double not null,
    Payment_Method varchar(35) not null
);

alter table Payment auto_increment=8000;
--Creating Booking
create table Booking_Details(
    Booking_ID int not null auto_increment primary key,
    Customer_ID int not null,
    From_Date date not null,
    Return_Date datetime not null,
    Amount double,
    Actual_Return_Date datetime not null,
    Pickup_Location int not null,
    Drop_Location int not null,
    Insurance int,
    Car_Reg_No char(6) not null,
    Payment_ID int,
    foreign key(Customer_ID) references Customer(Customer_ID),
    foreign key(Insurance) references Car_Insurance(Insurance_ID),
    foreign key(Pickup_Location) references Location(Location_ID),
    foreign key(Drop_Location) references Location(Location_ID),
    foreign key(Car_Reg_No) references car_detail(Registration_No),
    foreign key(Payment_ID) references Payment(Payment_ID)
    );

alter table Booking_Details auto_increment=9000;
