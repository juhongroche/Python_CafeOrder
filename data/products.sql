-- Adminer 4.8.1 PostgreSQL 17.0 (Debian 17.0-1.pgdg120+1) dump

DROP TABLE IF EXISTS "products";
CREATE TABLE "public"."products" (
    "product_id" integer DEFAULT GENERATED ALWAYS AS IDENTITY NOT NULL,
    "product" character varying(255) NOT NULL,
    "price" numeric NOT NULL,
    CONSTRAINT "products_pkey" PRIMARY KEY ("product_id")
) WITH (oids = false);

INSERT INTO "products" ("product_id", "product", "price") VALUES
(1,	'Americano',	3.0),
(2,	'Caffe Latte',	3.5),
(3,	'Cafe Mocha',	3.7),
(4,	'English Tea',	2.0),
(5,	'Fruit Tea',	2.0),
(6,	'Still Water',	1.5),
(7,	'Sparkling Water',	1.5),
(8,	'Coke Zero',	2.0),
(9,	'Coke 2.0',	2.0),
(10,	'Sprite Zero',	2.0),
(11,	'Sprite',	2.0),
(12,	'Milkshake',	4.0),
(13,	'Smoothie',	5.0),
(14,	'Lemonade',	2.5),
(15,	'Sandwich',	3.5),
(16,	'Pancake',	5.0),
(17,	'Muffin',	2.0),
(18,	'Soup',	5.5),
(19,	'Pizza',	15.0),
(20,	'Ice Cream',	3.0);

-- 2024-11-11 16:23:09.054649+00
