-- Adminer 4.8.1 PostgreSQL 17.0 (Debian 17.0-1.pgdg120+1) dump

\connect "mini_project";

DROP TABLE IF EXISTS "couriers";
CREATE TABLE "public"."couriers" (
    "courier_id" integer DEFAULT GENERATED ALWAYS AS IDENTITY NOT NULL,
    "courier_name" character varying(255) NOT NULL,
    "courier_phone" character varying(255) NOT NULL,
    CONSTRAINT "couriers_pkey" PRIMARY KEY ("courier_id")
) WITH (oids = false);


DROP TABLE IF EXISTS "orders";
CREATE TABLE "public"."orders" (
    "order_id" integer DEFAULT GENERATED ALWAYS AS IDENTITY NOT NULL,
    "customer_name" character varying(255) NOT NULL,
    "customer_address" character varying(255) NOT NULL,
    "customer_phone" character varying(255) NOT NULL,
    "product_id" character INTEGER NOT NULL,
    "courier_id" integer NOT NULL,
    "order_status" character varying(255) NOT NULL,
    CONSTRAINT "orders_pkey" PRIMARY KEY ("order_id")


) WITH (oids = false);

INSERT INTO "orders" ("order_id", "customer_name", "customer_address", "customer_phone", "product_id", "courier_id", "order_status") VALUES
(1,	'John',	'Unit 2, 12 Main Street, LONDON, WH1 2ER',	'0789887334',	'1',	2,	'PREPARING'),
(2,	'Alex',	'55 Oxford Street, LONDON, WC51 1TU',	'0785786178',	'1',	3,	'PREPARING'),
(3,	'Lily',	'180 Bond Street, LONDON, W5 9QM',	'0756549568',	'4',	5,	'PREPARING'),
(4,	'Ted',	'123 London road, London,  W1 2MA',	'07973648576',	'17',	2,	'PREPARING'),
(5,	'Jane',	'Flat 222, Onion street, Dorset, DO12 3RT',	'0712354556',	'12',	2,	'PREPARING'),
(6,	'Liam',	'123 Sydney Road, Sydney SY13 5UT',	'0729485949',	'4',	2,	'PREPARING'),
(7,	'Mia',	'67 Mia Road, Mia MI13 6YU',	'073949696',	'2',	2,	'PREPARING'),
(8,	'William',	'1 Prince Road, London WC1 1WC',	'0729485475',	'9',	5,	'PREPARING'),
(9,	'Sally',	'12 Brixton Road, London SE20 3TU',	'0739459667',	'10',	4,	'PREPARING'),
(10,	'Ben',	'30 Ben Road, Ben BE14 5YU',	'0729394964',	'11',	3,	'PREPARING');

DROP TABLE IF EXISTS "products";
CREATE TABLE "public"."products" (
    "product_id" integer DEFAULT GENERATED ALWAYS AS IDENTITY NOT NULL,
    "product" character varying(255) NOT NULL,
    "price" numeric NOT NULL,
    CONSTRAINT "products_pkey" PRIMARY KEY ("product_id")
) WITH (oids = false);


-- 2024-11-13 22:54:44.688698+00
