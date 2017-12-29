from django.urls import include, path, re_path

from rest_framework import routers

from oo.api.v1 import views
from oo.users.views import OTPRegister, OTPLogin

router = routers.DefaultRouter()

router.register(r'types', views.TypeViewSet)
router.register(r'instances', views.InstanceViewSet)
router.register(r'topics', views.TopicViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'currencies', views.CurrencyViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'interactions', views.InteractionViewSet)
router.register(r'contributions', views.ContributionViewSet)

router.register(r'topic_snapshots', views.TopicSnapshotViewSet)
router.register(r'comment_snapshots', views.CommentSnapshotViewSet)
router.register(r'hourprice_snapshots', views.HourPriceSnapshotViewSet)
router.register(r'currencyprice_snapshots', views.CurrencyPriceSnapshotViewSet)

router.register(r'user_balance', views.UserBalanceViewSet)
router.register(r'language_names', views.LanguageNameViewSet)


urlpatterns = [
    re_path('^$', views.schema_view),
    path('', include(router.urls)),
    path('otp/signup/', OTPRegister.as_view(), name="otp-signup"),
    path('otp/login/', OTPLogin.as_view(), name="otp-login")
]
