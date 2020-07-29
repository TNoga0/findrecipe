from django import forms


class IngredientInputForm(forms.Form):
    meal_type = forms.CharField(
        label="Select meal type",
        widget=forms.Select(choices=[
            ('breakfast', 'Breakfast'),
            ('dessert', 'Dessert'),
            ('main_course', 'Main course'),
            ('healthy', 'Healthy food'),
        ]),
    )
    contents = forms.CharField(
        max_length=500,
        widget=forms.Textarea(),
    )


class SelectMealTypeForm(forms.Form):
    selector=forms.CharField(
        label="Select Category",
        widget=forms.Select(choices=[
            ('breakfast', 'Breakfast'),
            ('dessert', 'Dessert'),
            ('main_course', 'Main course'),
            ('healthy', 'Healthy food'),
        ])
    )
