create table wm_shop(
    city_name varchar(20) not null,
    lat int(10) not null,
    lng int(10) not null,
    shop_id varchar(20) not null,
    shop_name varchar(50) not null,
    shop_score char(3),
    month_sales varchar(20),
    shop_pic_url varchar(100),
    delivery_time varchar(20),
    start_price varchar(20),
    shipping_send_price varchar(20),
    average_price varchar(20),
    shipping_time_info varchar(100),
    distance varchar(20),
    address varchar(100)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;