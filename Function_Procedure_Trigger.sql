--Function Call
select b.Booking_ID,Total_Cost(b.From_Date,b.Return_Date,b.Actual_Return_Date,cat.category_name) as Amount 
from (( booking_details as b inner join car_detail as car on b.Car_Reg_No = car.Registration_No ) 
inner join car_category as cat on car.Category = cat.category_name);



--Creating a view to store the Result returned by the Function 
create view BookingAmount as select b.Booking_ID as Booking_ID,Total_Cost(b.From_Date,b.Return_Date,b.Actual_Return_Date,cat.category_name) as Amount 
from (( booking_details as b inner join car_detail as car on b.Car_Reg_No = car.Registration_No ) 
inner join car_category as cat on car.Category = cat.category_name);



--Updating the Amount field in Booking_Details 
UPDATE booking_details AS b INNER JOIN BookingAmount AS b1 ON b.Booking_ID = b1.Booking_ID SET b.Amount = b1.Amount;


--Trigger :
--Set the availability of a particular car to 0 when that car is booked.
drop trigger if exists booking_done;
delimiter $$
create trigger booking_done
after insert
on booking_details for each row
begin

update car_detail set Availability =0 where Registration_No = new.Car_Reg_No;

end $$
delimiter ;

--inserting Data
insert into Booking_Details(Customer_ID,From_Date,Return_Date,Amount,Actual_Return_Date,Pickup_Location,Drop_Location,Insurance,Car_Reg_No,Payment_ID)
values
(5005,"2022-11-14","2022-11-20 9:00",0,"2022-11-20 9:00",6000,6003,7001,"UI1289",8000);


--Procedure along with cursor:
DELIMITER $$
CREATE PROCEDURE Update_Payment() 
BEGIN
DECLARE done INT DEFAULT 0;
DECLARE Amt double;
DECLARE pay_id int(11);
DECLARE booking_cursor CURSOR FOR SELECT Amount,Payment_ID FROM booking_details;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
OPEN booking_cursor;
label: LOOP
FETCH booking_cursor INTO Amt,pay_id;
UPDATE Payment set Total_Amount = Amt where Payment_ID = pay_id;
IF done = 1 THEN LEAVE label;
END IF;
END LOOP;
CLOSE booking_cursor;
END $$

DELIMITER ;