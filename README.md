# EduNexus

MVP учебной платформы на Django с базовыми сущностями:
- Профиль пользователя с ролью (`teacher` / `student`)
- Курсы
- Уроки
- Материалы урока (видео, документ, ссылка)

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

После запуска:
- Админ-панель: `http://127.0.0.1:8000/admin/`
- Список курсов: `http://127.0.0.1:8000/`

---

## Почему появляется ошибка `Not Found`

Обычно это одна из причин:

1. **Django-сервер не запущен**.
2. Вы открываете не тот адрес или порт.
3. Зависимости не установлены (`ModuleNotFoundError: No module named 'django'`).
4. Миграции не применены.

### Чеклист исправления

1. Активируйте окружение:
   ```bash
   source .venv/bin/activate
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Примените миграции:
   ```bash
   python manage.py migrate
   ```
4. Запустите сервер:
   ```bash
   python manage.py runserver 127.0.0.1:8000
   ```
5. Откройте в браузере:
   - `http://127.0.0.1:8000/`

> Если вы запускаете через контейнер/удалённую машину, иногда нужен адрес `0.0.0.0:8000`:
> ```bash
> python manage.py runserver 0.0.0.0:8000
> ```

---

## Как установить `requirements.txt`, если есть проблемы с сетью/прокси

Если обычная команда не работает:

```bash
pip install -r requirements.txt
```

используйте один из вариантов ниже.

### 1) Проверить/очистить прокси переменные

```bash
env | rg -i 'proxy'
unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY
pip install -r requirements.txt
```

### 2) Явно указать официальный индекс PyPI

```bash
pip install -r requirements.txt -i https://pypi.org/simple
```

### 3) Использовать внутренний корпоративный mirror (если есть)

```bash
pip install -r requirements.txt -i <YOUR_INTERNAL_PYPI_URL>
```

### 4) Установка офлайн (если интернет полностью закрыт)

На машине с интернетом:
```bash
pip download -r requirements.txt -d wheelhouse
```

Перенесите папку `wheelhouse` в сервер и установите:
```bash
pip install --no-index --find-links=wheelhouse -r requirements.txt
```

---

## Проверка после установки

```bash
python -c "import django; print(django.get_version())"
python manage.py check
python manage.py test
```

## Тесты

```bash
python manage.py test
```
