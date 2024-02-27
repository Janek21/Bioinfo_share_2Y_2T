
--Products
insert into Product (Name, Brand, Price, Stock, Barcode) values ('Milk', 'Vacona', '0,75', 50, '56790A'); 
insert into product (Name, Brand, Price, Stock, Barcode) values ('Milk', 'La Munyidora', '1,25', 70, '12345Z'); 
insert into product (Name, Brand, Price, Stock, Barcode) values ('Beer', 'El monjo', '2,15', 100, '12345Z'); 

--Ticket
insert into Ticket (Box, TicketDate, FormPayment, Total) values (3, to_date('30/09/18','DD/MM/YY'), 'card','3'); 
insert into ticket (Box, TicketDate, FormPayment, Total) values (3, to_date('01/10/18','DD/MM/YY'), 'card','3,25');
insert into ticket (Box, TicketDate, FormPayment, Total) values (1, to_date('30/09/18','DD/MM/YY'), 'cash','3,4');

--Sale
insert into Sale (Product_barcode, Ticket_box, Ticket_date, units) values ('54389Q', 3, to_date('01/10/18','DD/MM/YY'), 11); 
insert into sale (Product_barcode, Ticket_box, Ticket_date, units) values ('12345Z', 3, to_date('01/10/18','DD/MM/YY'), 3); 
insert into sale (Product_barcode, Ticket_box, Ticket_date, units) values ('12345Z', 3, to_date('01/10/18','DD/MM/YY'), 10); 

commit