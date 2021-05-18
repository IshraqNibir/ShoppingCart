# ShoppingCart

This is a project where an user can enter his information and buy products. After buying his needs an invoice will be generated with qr code.


TECHNOLOGY USED:
1. Python(django)
2. DBSQLITE
3. HTML,CSS
4. Javascript


ADMIN MANUAL:
--> The admin must create a superuser for inserting data in the products table.
--> The products that the customer/user will get, it will come from the products table that the superuser inserts.
--> There is a history model which stores all the information for future needs.


USER MANUAL:
--> After starting the project there is a home page, which consists the information of the company (bla bla bla).
--> From the home page user has to click 'Buy Items' to buy his daily needs.
--> After that the user will be redirected to the page where he has to enter his own information(Name, Email, Phone). All the fields are mandatory.
--> After the successful entrance of the information of the user he will be redirected to the page where he can select the product and quantity that he wants to   buy.
--> If the user put the quantity more than the stock of that particular product then a message will be given.
--> After selecting the product and quantity it will be added to cart. User can add as many products as he wants to the cart.
--> After adding users neccessary products to the cart he can find out from the cart which products he selected and how much the quantity is.
--> Then he can confirm the order and an invoice will be generated.
--> The invoice will be in the pdf format and there is also an qr code in the invoice which consists of the information of the user.
--> User can download the pdf invoice for further reference.
