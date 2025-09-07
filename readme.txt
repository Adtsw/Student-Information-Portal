HOW TO CONNECT TO MYSQL AND CHANGE PASSWORD

mysql -u root -> opens mysql in terminal

ALTER USER user(root)@host(localhost) IDENTIFIED BY 'new password as put in env';
FLUSH PRIVILEGES;

\q -> get out

mysql -u user(root) -p -> will ask for the password

Try to establish connection in DB UI


FOR ESTABLISHING PYTHON CONNECTION WITH YOUR DB

brew services start mysql -> allows to run in the bg for queries to run properly