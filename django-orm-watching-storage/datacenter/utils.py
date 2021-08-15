import datetime

from .models import Visit


def format_duration(duration: datetime.timedelta) -> str:
    seconds_to_transform = duration.total_seconds()
    hours, time_remainder = divmod(seconds_to_transform, 60 * 60)
    minutes, seconds = divmod(time_remainder, 60)

    time_template = "{:.0f}:{:.0f}:{:.0f}"
    time_repr = time_template.format(hours, minutes, seconds)

    return time_repr


def to_dict(instance: Visit,
            instances_fields_names=("who_entered", "entered_at", "duration", )):

    owner_name = instance.passcard.owner_name
    entered_at = instance.entered_at
    duration = format_duration(instance.get_duration())

    instances_fields_vals = (owner_name, entered_at, duration)

    instance_part = zip(instances_fields_names, instances_fields_vals)

    about_instance = {}
    for field_name, field_value in instance_part:
        about_instance[field_name] = field_value

    return about_instance
