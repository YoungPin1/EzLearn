<div align="center">

# **EzLearn**

*Приложение для изучения и запоминания новой информации через создание карточек и тестов.*

</div>

### 1. Окно регистрации

При входе в приложение пользователю будет предоложено зарегистрироваться или войти в свой аккаунт. 
После ввода данных приложение свяжется с базой данных и войдет в приложение, либо выведет ошибку,
если пользователь некоррекно пытался авторизироваться.\
![authorization](https://user-images.githubusercontent.com/92945480/140500456-1648771b-7602-4186-a3f4-34dd759e000b.png)\
Функционал предствлен в классе Authorization

### 2. Основное меню

В основном меню в QScrollArea будет показаны все модули пользователя в виде плитки, нажав на которую
будет открыто меню заучивания.\
Также можно нажать на кнопку __Создать новый модуль__, чтобы войти в меню добавление модуля.\
![main](https://user-images.githubusercontent.com/92945480/140500538-a7785a1d-7a18-4c3d-bfba-030543bd4574.png)\
Функционал предствлен в классе EzMain

### 3. Заучивание

В этом меню заключается главная идея приложения. В нем отображены все слова и определения или переводы и
их значения их переводы или значения QTableEdit.\

Из этого меню можно редактировать модуль нажатием на кнопку, после чего пользователь будет перекинут в окно
редактирования.\
![learnmain](https://user-images.githubusercontent.com/92945480/140658834-cdec7e33-3ab7-40f3-8582-07538572e729.png)\
Если пользователь захочет удалить модуль, то сначала ему будет выведено предупреждение в виде 
QMessageBox, где он может подтвердить свои действия или отменить\
![delete_module](https://user-images.githubusercontent.com/92945480/140500830-485854d1-3f18-4991-a748-263efafb0d06.png)\
Программа сама считает прогресс и сохраняет его в базу данных, где 0 - слово неизчено совсем, 
1 - слово еще нужно повторить и 2 - слово изучено. Пользователю будет выведен общий прогресс в
QProgressBar, который можно сбросить, если есть нужда повторить информацию.\
Модуль можно скачать в .csv формате. При нажатии на кнопку, будет показано диалоговое окно с выбором
названия и место сохранения файла.\
![save](https://user-images.githubusercontent.com/92945480/140500851-0e034d24-90d5-4607-a49a-1936b56a5612.png)\
Из этого окна можно попасть в окна изучения:

* `Наизусть` - режим, в котором выводится значение и 4 разных варианта ответа. Пользвателю нужно выбрать правильный.
* `Карточки` - в этом режиме будет предложено значение слова. Нажатие на правую кнопку означает, что пользователь усвоил
  его, а на левую - что это слово нужно еще повторить
* `Письмо` - пользвателю дано значение, по которому он сам должен написать слово. Таким образом проверятеся знание
  правописания слова.
Функционал предствлен в классе MainLearn
### 4. Редактирование и создание 

При создании модуля пользователь задает ему имя, после чего начинает добавлять пары значений и слов вводя их в QTableView.
Пользователь может импортировать таблицу или .txt или .csv файла, после чего ему останется только ввести имя. Реализовано
с помощью диалогового окна. Также можно удалить карточку или добавить еще одну
После нажатия `Создать` пользователь создаст новую таблицу в базе данных в формате User_module_{}, где
последними символами будут являться id модуля.
![save](https://user-images.githubusercontent.com/92945480/140500939-1d156065-aa9c-43c0-8e3d-33451d2cc041.png)\
Функционал предствлен в классе AddModule

### 5. Заучивание

В QLineEdit выводится слово, к которому нужно подобрать правильный ответ нажатием на 1 из 4 кнопок. При правильном ответе кнопка 
загорится зеленым, а при неправильном - красным, а ответ выведется QLabel. Каждый блок состоит из 10 слов, но если слова кончатся,
то он завершится сам с выводом сообщения в QMessageBox. 
Функционал реализован в классе ByHeart
![learnwrite](https://user-images.githubusercontent.com/92945480/140659088-abce6e36-b156-4de8-afb2-0387974561d9.png)\

### 6. Письмо

Как и в заучивании, сверху экрана выведется определение, по которому нужно ввести правильный ответ и нажать QPushButton
__Ответить__. Если ответ правильный, он отметится зеленым цветом, если нет - красным и выведется в лэйбэл ниже. Каждый блок состоит из 10 слов, но если слова кончатся,
то он завершится сам с выводом сообщения в QMessageBox.\
![learnbh](https://user-images.githubusercontent.com/92945480/140659246-3284002f-99c5-4341-ad67-7f0884f4681a.png)\
Функционал представлен в калссе Write

### 7. Карточки

В центре этого окна будет кнопка с определением. Нажатием на нее пользователь увидит слово, а повторным - снова определение.
Нажатие на красную кнопку добавит слово в список неусвоенных, а на зеленую - в список выученных. Количество этих слов и общее количество указвается внизу экрана.\
Кнопка в левом верхем углу вернет в меню заучивания. При каждом действии программа будет связываться с базой данных и 
менять значение learning в таблице.
![cards](https://user-images.githubusercontent.com/92945480/140500994-8710eba3-29e4-4daa-91ba-c2b00b7f4e2d.png)\
Функционал предствлен в классе Cards

### 8. Структура базы данных
В базе данных есть 3 основные таблицы.
В главной таблице auth_data хранятся id, логин и пароль пользователя. id является внешним ключом к
id_user из таблицы user_modules, где хранятся уникальный module_id, module_name и is_deleted для данных
об удалении. В таблице words хранятся все данные в столбцах word_id - автоинкримент, word, meaning, module_id (внешним
ключем к нему является module_id из таблицы user_modules) и learning
![db_structure](https://user-images.githubusercontent.com/92945480/140659462-35ee987a-8a5f-488a-aa4b-1e87b8505593.png)


