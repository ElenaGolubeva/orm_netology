import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Stock, Sale, Shop, create_tables

connection_driver = 'postgresql'
login = 'postgres'
password = '29092003'
connection_name = 'localhost'
port = '5432'
db_name = 'homework_db'

DSN = f'{connection_driver}://{login}:{password}@{connection_name}:{port}/{db_name}'
#драйвер_подключения://пользователь:пароль@название_подключения:порт/имя_БД


engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

author1 = Publisher(name="Пушкин ")
author2 = Publisher(name="Достоевский")
author3 = Publisher(name="Тургенев")
author4 = Publisher(name="Островский")

session.add_all([author1, author2, author3, author4])
session.commit()

book1 = Book(name='Евгений Онегин', id_publisher=author1.id)
book2 = Book(name='Преступление и наказание', id_publisher=author2.id)
book3 = Book(name='Отцы и дети', id_publisher=author3.id)
book4 = Book(name='Бесприданница', id_publisher=author4.id)
book5 = Book(name='Капитанская дочка', id_publisher=author1.id)
book6 = Book(name='Идиот', id_publisher=author2.id)
book7 = Book(name='Муму', id_publisher=author3.id)
book8 = Book(name='Гроза', id_publisher=author4.id)
book9 = Book(name='Дубровский', id_publisher=author1.id)
session.add_all([book1, book2, book3, book4, book5, book6, book7, book8, book9])
session.commit()


shop1 = Shop(name='Буквоед')
shop2 = Shop(name='Лабиринт')
shop3 = Shop(name='Читай город')
shop4 = Shop(name='Чук и Гек')
session.add_all([shop1, shop2, shop3, shop4])
session.commit()

stock1 = Stock(id_book=book1.id, id_shop=shop1.id, count=20)
stock2 = Stock(id_book=book2.id, id_shop=shop2.id, count=22)
stock3 = Stock(id_book=book3.id, id_shop=shop3.id, count=24)
stock4 = Stock(id_book=book4.id, id_shop=shop4.id, count=21)
stock5 = Stock(id_book=book5.id, id_shop=shop1.id, count=100)
stock6 = Stock(id_book=book6.id, id_shop=shop2.id, count=15)
stock7 = Stock(id_book=book7.id, id_shop=shop3.id, count=12)
stock8 = Stock(id_book=book8.id, id_shop=shop4.id, count=34)
stock9 = Stock(id_book=book9.id, id_shop=shop1.id, count=2)
stock10 = Stock(id_book=book1.id, id_shop=shop2.id, count=12)
stock11 = Stock(id_book=book2.id, id_shop=shop3.id, count=19)
stock12 = Stock(id_book=book3.id, id_shop=shop4.id, count=27)
stock13 = Stock(id_book=book4.id, id_shop=shop1.id, count=39)
stock14 = Stock(id_book=book5.id, id_shop=shop2.id, count=15)
session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9, stock10, stock11, stock12, stock13, stock14])
session.commit()


sale1 = Sale(price=250, date_sale='23.10.2023', id_stock=stock1.id, count=3)
sale2 = Sale(price=300, date_sale='23.10.2023', id_stock=stock2.id, count=4)
sale3 = Sale(price=350, date_sale='23.10.2023', id_stock=stock3.id, count=5)
sale4 = Sale(price=200, date_sale='23.10.2023', id_stock=stock4.id, count=7)
sale5 = Sale(price=250, date_sale='23.10.2023', id_stock=stock5.id, count=1)
sale6 = Sale(price=300, date_sale='23.10.2023', id_stock=stock6.id, count=2)
sale7 = Sale(price=350, date_sale='23.10.2023', id_stock=stock7.id, count=5)
sale8 = Sale(price=200, date_sale='23.10.2023', id_stock=stock8.id, count=3)
sale9 = Sale(price=250, date_sale='23.10.2023', id_stock=stock9.id, count=7)
sale10 = Sale(price=300, date_sale='23.10.2023', id_stock=stock10.id, count=9)
sale11 = Sale(price=350, date_sale='23.10.2023', id_stock=stock11.id, count=12)
sale12 = Sale(price=200, date_sale='23.10.2023', id_stock=stock12.id, count=4)
sale13 = Sale(price=250, date_sale='23.10.2023', id_stock=stock13.id, count=2)
sale14 = Sale(price=300, date_sale='23.10.2023', id_stock=stock14.id, count=6)

session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10, sale11, sale12, sale13])
session.commit()

def get_shops(author):
    query = session.query(Book.name, Shop.name, Sale.price*Sale.count, Sale.date_sale).select_from(Book).join(Stock).join(Shop).join(Publisher).join(Sale)
    if author.isdigit():
        query = query.filter(Publisher.id == int(author)).all()
    else:
        query = query.filter(Publisher.name.like(f'%{result}%')).all()
    for book_name, shop_name, price, date_sale in query:
        print(f"{book_name: <40} | {shop_name: <10} | {price: <8} | {date_sale.strftime('%d-%m-%Y')}")


if __name__ == "__main__":
    result = input("Введите автора: ")
    get_shops(result)

session.close()