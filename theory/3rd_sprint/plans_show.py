# project urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("plans/", include("practice.urls")),
]

# application urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]

# application views.py

# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # Доступные тарифные планы
    plans = [
        {
            "name": "Бесплатно",
            "price": "0",
            "options": {"users": 10, "space": 10,
                        "support": "Почтовая рассылка"},
        },
        {
            "name": "Профессиональный",
            "price": "49",
            "options": {"users": 50, "space": 100,
                        "support": "Телефон и email"},
        },
        {
            "name": "Корпоративный",
            "price": "99",
            "options": {"users": 100, "space": 500,
                        "support": "Персональный менеджер"},
        },
    ]

    return render(request, 'index.html', {"plans": plans})
# HttpResponse("Hello, world!")

# application index.html
<!DOCTYPE html>
<!-- Based on https://getbootstrap.com/docs/4.4/examples/pricing/ -->
<html lang="ru">
  <head>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <title>Всяческие услуги</title>

    <!-- Bootstrap core CSS -->
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
      crossorigin="anonymous"
    />
  </head>

  <body>
    <div
      class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm"
    >
      <h5 class="my-0 mr-md-auto font-weight-normal">Всяческие услуги</h5>
    </div>

    <div class="pricing-header px-3 py-3 pt-md-5 pb-md-4 mx-auto text-center">
      <h1 class="display-4">Тарифы</h1>
      <p class="lead">
        Ознакомьтесь с нашими тарифами и закажите услугу.
      </p>
    </div>
    {% for item in plans %}

    <div class="container">
      <div class="card-deck mb-3 text-center">
        <div class="card mb-4 shadow-sm">
          <div class="card-header">
            <h4 class="my-0 font-weight-normal">{{ item.name }}</h4>
          </div>
          <div class="card-body">
            <h1 class="card-title pricing-card-title">
              $ {{ item.price }}<small class="text-muted">/ в месяц</small>
            </h1>
            <ul class="list-unstyled mt-3 mb-4">
              <li>{{ item.options.users }} пользователей</li>
              <li>{{ item.options.space }} GB места</li>
              <li>Поддержка: {{ item.options.support }}</li>
            </ul>
            <a
              href="mailto:order@company.site?subject=Услуга {{ item.name }}"
              class="btn btn-lg btn-block btn-outline-primary"
            >
              Связаться
          </a>
          </div>
        </div>
      </div>
    {% endfor %}

      <footer class="pt-4 my-md-5 pt-md-5 border-top">
        <div class="row">
          <div class="col-12 col-md">
            Всяческие услуги
            <small class="d-block mb-3 text-muted">&copy; 3020</small>
          </div>
        </div>
      </footer>
    </div>

  </body>
</html>
