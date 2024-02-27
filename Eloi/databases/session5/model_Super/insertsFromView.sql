insert into Product  (Name, Brand, Price, Stock, Barcode)
   Select distinct  NameProduct, NameBrand, PriceUnit, Stock, Barcode from importexcel;

insert into Ticket (Box, TicketDate, FormPayment, Total)
   Select distinct Box, DateSale, FormPayment,PriceSale from importexcel;
   
insert into Sale (Product_barcode, Ticket_box, Ticket_date, units)
   Select Barcode, Box, DateSale, UnitsSale from importexcel;
   
commit;