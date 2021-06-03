from django.forms import ModelForm, Select, CheckboxInput
from .models import TodoList


locations = (
    ("Aberdeen", "Aberdeen"),
    ("Birmingham", "Birmingham"),
    ("Cardiff", "Cardiff"),
    ("Dundee", "Dundee"),
    ("Guildford", "Guildford"),
    ("Plymouth", "Plymouth"),
    ("Portsmouth", "Portsmouth"),
    ("Manchester", "Manchester"),
    ("Swansea", "Swansea"),
    ("Truro", "Truro"),
)


# Create a form.
class TodoListForm(ModelForm):
    # Create meta class to specify the model to use.
    class Meta:
        model = TodoList
        fields = ['done', 'title', 'location', 'due_date']

        widgets = {
            'location': Select(choices=locations, attrs={'class': 'form-control'}),
            'done': CheckboxInput(attrs={'onclick': 'this.form.submit();'}),
        }
