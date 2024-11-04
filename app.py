from flask import Flask, render_template

app = Flask(__name__)

# Lijst van gerechten met allergenen en alerts
gerechten = [

    {
        'naam': 'Liflafjes',
        'allergenen': ['Ei', 'Gluten', 'Melk', 'Mosterd', 'Soja', 'Sesamzaad', 'Vis']
    },
    {
        'naam': 'Broodje Kiep',
        'allergenen': ['Soja']
    },
    {
        'naam': 'Tosti de Hebberd',
        'allergenen': ['Melk']
    },
    {
        'naam': 'Avocado Zalm',
        'allergenen': ['Vis']
    },
    {
        'naam': 'Ossenhaaspuntjes',
        'allergenen': ['Soja']
    },
    {
        'naam': 'Knolselderij Carpaccio',
        'allergenen': ['Selderij']
    },
    {
        'naam': 'Tonijnsalade',
        'allergenen': ['Ei', 'Melk', 'Mosterd', 'Vis']
    },
    {
        'naam': 'Pulled Chicken',
        'allergenen': ['Soja', 'Zwaveldioxide']
    },
    {
        'naam': 'Gesmolten Toestand',
        'allergenen': ['Melk']
    },
    {
        'naam': 'Salade Vis',
        'allergenen': ['Vis']
    },
    {
        'naam': 'Salade Kip',
        'allergenen': ['Soja']
    },
    {
        'naam': 'Uitsmijter de Hebberd',
        'allergenen': ['Ei']
    },
    {
        'naam': 'Uitsmijter Kaas',
        'allergenen': ['Melk', 'Ei']
    },
    {
        'naam': 'Uitsmijter Ham of Spek',
        'allergenen': ['Ei']
    },
    {
        'naam': 'Uitsmijter Ham/Spek en Kaas',
        'allergenen': ['Ei', 'Melk']
    },
    {
        'naam': 'Omelet de Hebberd',
        'allergenen': ['Ei', 'Melk', 'Selderij']
    },
    {
        'naam': 'Omelet Kaas',
        'allergenen': ['Ei', 'Melk', 'Selderij']
    },
    {
        'naam': 'Omelet Ham/Spek',
        'allergenen': ['Ei', 'Melk', 'Selderij']
    },
    {
        'naam': 'Omelet Ham/Spek en Kaas',
        'allergenen': ['Ei', 'Melk', 'Selderij']
    },
    {
        'naam': 'Kipburger',
        'allergenen': ['Gluten', 'Selderij']
    },
    {
        'naam': 'Tosti Brie',
        'allergenen': ['Melk']
    },
    {
        'naam': 'Tosti de Hebberd',
        'allergenen': ['Melk']
    },
    {
        'naam': 'Chinese Tomatensoep',
        'allergenen': ['Selderij']
    },
    {
        'naam': "Opa's Kerriesoep",
        'allergenen': ['Melk']
    },
    {
        'naam': 'Rundvlees Kroketten',
        'allergenen': ['Gluten', 'Melk', 'Selderij']
    },
    {
        'naam': 'Groente Kroketten',
        'allergenen': ['Gluten', 'Lupine', 'Soja']
    },

    {
        'naam': "'t haasje zijn",
        'allergenen': ['Soja-alert', 'Ei', 'Gluten']
    },

        {
        'naam': 'Chinese Tomatensoep',
        'allergenen': ['Selderij']
    },
    {
        'naam': "Opa's Kerriesoep",
        'allergenen': ['Melk']
    },
    {
        'naam': 'Knolselderij carpaccio',
        'allergenen': ['Selderij']
    },
    {
        'naam': 'Yin & Yang',
        'allergenen': ['Soja']
    },
    {
        'naam': 'Gamba Bijeenkomst',
        'allergenen': ['Schaaldieren', 'Soja']
    },
    {
        'naam': 'Knabbeljauw',
        'allergenen': ['Ei', 'Gluten', 'Vis']
    },
    {
        'naam': 'Truffelpasta',
        'allergenen': ['Gluten', 'Ei', 'Melk']
    },
    {
        'naam': 'Risotto',
        'allergenen': ['Melk', 'Soja']
    },
    {
        'naam': 'Kluivertjes',
        'allergenen': ['Soja']
    },
    {
        'naam': 'Kipburger',
        'allergenen': ['Gluten', 'Selderij']
    },
    {
        'naam': 'Kenniekieze',
        'allergenen': ['Gluten']
    },
    {
        'naam': 'Vlinders in de buik',
        'allergenen': ['Selderij', 'Soja']
    },
    {
        'naam': 'Dat wordt Lappen',
        'allergenen': ['Ei', 'Gluten']
    },
    {
        'naam': 'Liflaf',
        'allergenen': ['Gluten', 'Ei', 'Noten', 'Pinda', 'Melk']
    },
    {
        'naam': 'Dame Blanche',
        'allergenen': ['Melk']
    },
    {
        'naam': 'Cheesecake',
        'allergenen': ['Gluten', 'Melk']
    },
    {
        'naam': 'Crème Brûlée',
        'allergenen': ['Ei', 'Melk']
    },
    {
        'naam': 'Tiramisu',
        'allergenen': ['Gluten', 'Melk', 'Ei']
    },
    {
        'naam': 'Apfelstrudel',
        'allergenen': ['Gluten', 'Melk']
    },
    {
        'naam': 'Perzik Crumble',
        'allergenen': ['Gluten', 'Melk', 'Noten']
    },
    {
        'naam': 'Koffie Compleet',
        'allergenen': ['Gluten', 'Melk', 'Noten', 'Pinda']
    },


]

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
