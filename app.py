from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for the libraries
LIBRARIES_DATA = [
    {
        "id": 1,
        "name": "The Long Room",
        "location": "Dublin, Ireland",
        "image": "the_long_room.jpg",
        "description": "One of the most beautiful libraries in the world, located in Trinity College Dublin."
    },
    {
        "id": 2,
        "name": "NY Public Library",
        "location": "New York, USA",
        "image": "NY.jpg",
        "description": "A landmark with iconic architecture and vast collections."
    },
    {
        "id": 3,
        "name": "Austrian National Library",
        "location": "Vienna, Austria",
        "image": "austrian_national.jpg",
        "description": "Features the stunning State Hall with baroque design."
    },
        {
        "id": 4,
        "name": "Starfield Library",
        "location": "Seoul, South Korea",
        "image": "starfield.png",
        "description": "Grand, photogenic design and towering bookshelves, creating an Instagram-worthy atmosphere"
    }
]

@app.route('/')
def home():
    """Renders the main page with the list of libraries."""
    return render_template('index.html', libraries=LIBRARIES_DATA)

@app.route('/library/<int:library_id>')
def library_detail(library_id):
    """Renders the detail page for a specific library."""
    library = next((item for item in LIBRARIES_DATA if item["id"] == library_id), None)
    
    if library is None:
        # Simple error handling
        return render_template('404.html'), 404 
    
    return render_template('detail.html', library=library)


if __name__ == '__main__':
    # You would install Flask first: pip install Flask
    app.run(debug=True)