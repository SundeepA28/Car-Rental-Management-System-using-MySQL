--Join Operations
--Getting Car details along with its current Location.
select Registration_No,Model,Area,city,state from car_detail join location WHERE car_detail.Location = location.Location_ID;


--Display the First Name and Last Name of the User Who done a booking.
select Firstname,Lastname from customer join booking_details where customer.Customer_ID = booking_details.Customer_ID;

--Display Car Details along with along with the category to which it belongs, No of persons it can hold, Cost per day
select Model,Make,Category,cost_per_day,no_of_persons from car_detail join car_category WHERE car_detail.Category = car_category.category_name;


--Display the cars that have been selected by a customer.
select Firstname,Lastname,Make,Model,Category from customer join (booking_details join car_detail) where customer.Customer_ID = booking_details.Customer_ID and Registration_No = Car_Reg_No;


--Aggrigate Functions:
--Caluclate the number of cars  per each category:
select category,count(Registration_No) from car_detail group by category;

--Calculate the Number of people that are form the same Area.
select Address, count(Firstname) from customer group by Address;

--Average Amount per Transaction:
select AVG(Total_Amount) from payment;

--Number of car of a particular Model_year
select Model_Year, count(Registration_No) from car_detail group by Model_Year;


--SET Operations:
--Display the Customer First name and Last Name who have returned the Car on or before the Return Date
select Firstname,Lastname from customer join booking_details where customer.Customer_ID = booking_details.Customer_ID and Return_Date = Actual_Return_Date
UNION
select Firstname,Lastname from customer join booking_details where customer.Customer_ID = booking_details.Customer_ID and Return_Date > Actual_Return_Date;

--Display the First Name and Last Name of the Customer who have booked a car and are Male.
select Firstname,Lastname from customer where Gender = "Male"
INTERSECT
select Firstname,Lastname from customer join booking_details where customer.Customer_ID = booking_details.Customer_ID;

--Display the Customer Firstname and Last name where the Amount paid >2000 and is not Male
select Firstname,Lastname from customer join (booking_details join payment) where customer.Customer_ID = booking_details.Customer_ID and booking_details.Payment_ID = payment.Payment_ID and Total_Amount > 1250
EXCEPT
select Firstname,Lastname from customer where Gender="Male";

--Display the Car that were Booked and the Model_Year >2017
select Make,Model,Model_Year from car_detail join booking_details where Registration_No = Car_Reg_No
EXCEPT
select Make,Model,Model_Year from car_detail where Model_Year <= 2017;
