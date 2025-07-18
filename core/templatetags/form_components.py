from django import template

register = template.Library()

@register.inclusion_tag('components/form_input.html')
def form_input(field, label=None, input_type="text", placeholder=""):
    return {
        'field': field,
        'label': label or field.label,
        'input_type': input_type,
        'placeholder': placeholder,
        'id_for_label': field.id_for_label if hasattr(field, 'id_for_label') else "",
        'name': field.html_name if hasattr(field, 'html_name') else field.name if hasattr(field, 'name') else "",
    }
