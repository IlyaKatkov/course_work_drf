from rest_framework import serializers
from habits.models import Habit, NiceHabit
from habits.validators import check_duration_time, check_habit_periodicity, validate_fields


class HabitSerializer(serializers.ModelSerializer):
    duration_time = serializers.TimeField(validators=[check_duration_time])
    periodicity = serializers.IntegerField(validators=[check_habit_periodicity])

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        if data.get('reward'):
            reward = data.get('reward')
        else:
            reward = None
        if data.get('associated_nice_habit'):
            associated_nice_habit = data.get('associated_nice_habit')
        else:
            associated_nice_habit = None
        validate_fields(reward, associated_nice_habit)
        return data


class PublicHabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ["action", "place", "time", "reward", "associated_habit", "periodicity",
                  "time_for_habit", "is_public"]


class NiceHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = NiceHabit
        fields = "__all__"