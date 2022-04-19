from .constants import DEFAULT


def get_view_attr(view, attr_name, action=None):
    attr = getattr(view, attr_name)

    if not isinstance(attr, dict):
        return attr

    assert DEFAULT in attr, (
        f"Please specify default value using DEFAULT object as a key when using "
        f"'{attr_name}' as dictionary on '{view.__class__.__name__}'"
    )

    return attr.get(action or view.action, attr[DEFAULT])
