from rest_framework import generics
from habits.models import Habit, NiceHabit
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner
from habits.serializers import HabitSerializer, PublicHabitsSerializer, NiceHabitSerializer
from habits.paginators import HabitsPagination


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitsPagination

    def get_queryset(self):
        list_habits = super().get_queryset()
        return list_habits.filter(user=self.request.user)


class HabitsPublicListAPIView(generics.ListAPIView):
    serializer_class = PublicHabitsSerializer
    queryset = Habit.objects.all().filter(is_public=True)
    permission_classes = [IsAuthenticated]
    pagination_class = HabitsPagination


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class NiceHabitCreateAPIView(generics.CreateAPIView):
    serializer_class = NiceHabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_nice_habit = serializer.save()
        new_nice_habit.user = self.request.user
        new_nice_habit.save()


class NiceHabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class NiceHabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class NiceHabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class NiceHabitListAPIView(generics.ListAPIView):
    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitsPagination

    def get_queryset(self):
        list_nice_habits = super().get_queryset()
        return list_nice_habits.filter(user=self.request.user)