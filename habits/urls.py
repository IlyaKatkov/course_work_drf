from habits.apps import HabitsConfig
from django.urls import path
from habits.views import HabitListAPIView, HabitDestroyAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitCreateAPIView, HabitsPublicListAPIView, NiceHabitCreateAPIView, NiceHabitDestroyAPIView, \
    NiceHabitListAPIView, NiceHabitUpdateAPIView, NiceHabitRetrieveAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habit/', HabitListAPIView.as_view(), name='own_habits_list'),
    path('habit/public/', HabitsPublicListAPIView.as_view(), name='public_habits_list'),
    path('nice_habit/create/', NiceHabitCreateAPIView.as_view(), name='nice_habit_create'),
    path('nice_habit/delete/<int:pk>/', NiceHabitDestroyAPIView.as_view(), name='nice_habit_delete'),
    path('nice_habit/update/<int:pk>/', NiceHabitUpdateAPIView.as_view(), name='nice_habit_update'),
    path('nice_habit/<int:pk>/', NiceHabitRetrieveAPIView.as_view(), name='nice_habit_detail'),
    path('nice_habit/', NiceHabitListAPIView.as_view(), name='nice_habit_list'),
]