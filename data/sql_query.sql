CREATE TABLE orders(
    order_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
    customer_name character varying(255) NOT NULL,
    customer_address character varying(255) NOT NULL,
    customer_phone character varying(255) NOT NULL,
    product_id integer NOT NULL,
    courier_id integer NOT NULL,
    order_status integer NOT NULL,
    FOREIGN KEY(product_id) REFERENCES products(product_id),
    FOREIGN KEY(courier_id) REFERENCES couriers(courier_id),
    FOREIGN KEY(order_status) REFERENCES order_status(id),
    PRIMARY KEY (order_id)
);


INSERT INTO orders (customer_name, customer_address, customer_phone, product_id, courier_id, order_status)
VALUES ('John',	'Unit 2, 12 Main Street, LONDON, WH1 2ER',	'0789887334',	1,2,1),
        ('Alex',	'55 Oxford Street, LONDON, WC51 1TU',	'0785786178',	4,5,1),
        ('Lily',	'180 Bond Street, LONDON, W5 9QM',	'0756549568',	9,1,1),
        ('Ted',	'123 London road, London,  W1 2MA',	'07973648576',	15,3,1),
        ('Jane',	'Flat 222, Onion street, Dorset, DO12 3RT',	'0712354556',12,6,1),
        ('Liam',	'123 Sydney Road, Sydney SY13 5UT',	'0729485949',	17,2,1),
        ('Mia',	'67 Mia Road, Mia MI13 6YU',	'073949696',	3,5,1),
        ('William',	'1 Prince Road, London WC1 1WC',	'0729485475',	14,3,1),
        ('Sally','12 Brixton Road, London SE20 3TU',	'0739459667',	10,2,1),
        ('Ben',	'30 Ben Road, Ben BE14 5YU',	'0729394964',	9,4,1),
        ('Mary','293 Mary Road',	'072939456',	12,2,1);



CREATE TABLE products(
product_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
product VARCHAR(255) NOT NULL,
price DECIMAL NOT NULL,
PRIMARY KEY (product_id)
);


INSERT INTO products (product, price) VALUES
('Americano',	3.0),
('Caffe Latte',	3.5),
('Cafe Mocha',	3.7),
('English Tea',	2.0),
('Fruit Tea',	2.0),
('Still Water',	1.5),
('Sparkling Water',	1.5),
('Coke Zero',	2.0),
('Coke',	2.0),
('Sprite Zero',	2.0),
('Sprite',	2.0),
('Milkshake',	4.0),
('Smoothie',	5.0),
('Lemonade',	2.5),
('Sandwich',	3.5),
('Pancake',	5.0),
('Muffin',	2.0),
('Soup',	5.5),
('Pizza',	15.0),
('Ice Cream',	3.0);


CREATE TABLE order_status(
id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
status VARCHAR(255),
PRIMARY KEY (id)
);

INSERT INTO order_status (status)
VALUES ('PREPARING'),
('PENDING'),
('OUT-FOR-DELIVERY'),
('DELIVERED');



CREATE TABLE couriers(
courier_id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
courier_name VARCHAR(255) NOT NULL,
courier_phone VARCHAR(255) NOT NULL,
PRIMARY KEY (courier_id)
);

INSERT INTO couriers (courier_name, courier_phone)
Values ('Deliveroo','0769385756'),
('Uber-Eat','0790482954'),
('Just-Eat','0783957582'),
('DPD','792847575'),
('DHL','079383722'),
('FEDEX','07039394859'),
('YODEL','07398272949'),
('UPS','0739472823'),
('Parcel Force','073949596
');
