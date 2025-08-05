import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books_added(self, collector):

        collector.add_new_book('Гордость и Предубеждение и Зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1 проверка некорректного названия

    @pytest.mark.parametrize('invalid_name', ['', 'A'*41, 'A'*42, 'A'*60])
    def test_add_new_book_invalid_name_not_added(self, collector, invalid_name):
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()

    #2 проверка добавления дубликатов

    def test_add_new_book_dupe_not_added(self, collector):
        collector.add_new_book('Как поймать монстра')
        collector.add_new_book('Как поймать монстра')

        books = collector.get_books_genre()
        assert 'Как поймать монстра' in books and len(books) == 1

    # 3 проверка установления жанра
    # заодно проверяется получение жанра по имени

    def test_set_book_genre_horror_set(self, collector):
        collector.add_new_book('Гордость и Предубеждение и Зомби')
        collector.set_book_genre('Гордость и Предубеждение и Зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и Предубеждение и Зомби') == 'Ужасы'

    # 4 установление жанра для несуществующей книги

    def test_set_book_genre_invalid_book_not_set(self, collector):
        collector.set_book_genre('Кармилла', 'Ужасы')
        assert collector.get_book_genre('Кармилла') is None

    # 5 некорректные жанры

    @pytest.mark.parametrize('invalid_genre', ['', 'Классика'])

    def test_set_book_genre_invalid_genre_not_set(self, collector, invalid_genre):
        collector.add_new_book('Улисс')
        collector.set_book_genre('Улисс', invalid_genre)
        assert collector.get_book_genre('Улисс') == ''

    # 6 список книг по жанру

    def test_get_books_with_specific_genre_horror_show_horror(self, collector):
        for book in ['Оно', 'Интервью с вампиром', 'Человек-невидимка']:
            collector.add_new_book(book)
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Интервью с вампиром', 'Ужасы')
        collector.set_book_genre('Человек-невидимка', 'Фантастика')
        
        horror_books = collector.get_books_with_specific_genre('Ужасы')
        assert 'Оно' in horror_books and 'Интервью с вампиром' in horror_books and len(horror_books) == 2

    # 7 детские книги
    def test_get_books_for_children_horror_and_cartoons_show_cartoons(self, collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Лунтик')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Лунтик', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Лунтик']

    # 8 добавление в избранное + список избранного

    def test_add_book_in_favorites_one_book_added(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        assert 'Оно' in collector.get_list_of_favorites_books()

    #9 удаление из избранного

    def test_delete_book_from_favorites_existing_book_deleted(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')
        assert 'Оно' not in collector.get_list_of_favorites_books()

    #10 добавление дубликата в избранное

    def test_add_book_in_favorites_dupe_not_added(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Оно')
        assert len(collector.get_list_of_favorites_books()) == 1

    #11 позитивная проверка get_books_genre

    def test_get_books_genre_one_book_show(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_genre() == {'Оно': 'Ужасы'}

    #12 добавление в избранное книги не из коллекции

    def test_add_book_in_favorites_book_not_in_collection_not_added(self, collector):
        collector.add_book_in_favorites('Оно')
        assert 'Оно' not in collector.get_list_of_favorites_books()